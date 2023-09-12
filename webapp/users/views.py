from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_202_ACCEPTED, HTTP_201_CREATED
from rest_framework.authentication import get_authorization_header

from users import serializers
from users.models import UserSite

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from rest_framework.permissions import AllowAny, IsAuthenticated

from users.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


@extend_schema_view(
    post=extend_schema( 
        summary='Register', tags=['User'],
        responses={ HTTP_201_CREATED:  serializers.CreateUserSerializer }  )    
)
class RegisterUserView(APIView):
    """
    Register User
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.CreateUserSerializer

    def post(self, request):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)



@extend_schema_view(
    post=extend_schema( 
        summary='Login', tags=['User'], )
)
class LoginUserView(APIView):
    """
    Login User
    """
    permission_classes = (AllowAny,) 
    serializer_class = serializers.LoginUserSerializer      

    def post(self, request):        
        user = UserSite.objects.filter(email=request.data['email']).first()
        if not user:
            raise APIException('User is not exist.')
        if not user.check_password(request.data['password']):
            raise APIException('Invalid password.')
        
        # generate token
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        
        response = Response()
        # set httponly cookie
        response.set_cookie( key='refreshToken', value=refresh_token, httponly=True )        
        response.data = {
            'accessToken': access_token,
            'user': serializers.LoginUserSerializer(user).data            
        }

        return response
    


class MyTokenObtainPairView(TokenObtainPairView): 

    permission_classes = (AllowAny,)     

    def post(self, request, *args, **kwargs):

        user = UserSite.objects.filter(email=request.data['email']).first()
        if not user:
            raise APIException('User is not exist.')
        if not user.check_password(request.data['password']):
            raise APIException('Invalid password.')

        response = super().post(request, *args, **kwargs)        

        access_token = response.data["access"]
        refresh_token = response.data["refresh"]

        response.set_cookie( key='refreshToken', value=refresh_token, httponly=True )        
        response.data = {
            'accessToken': access_token,   
            'user': serializers.LoginUserSerializer(user).data                     
        }
        return response


@extend_schema_view(
    get=extend_schema( 
        summary='Get current User', tags=['User'], )
)
class MeUserView(APIView):
    """
    Get current User
    """
    permission_classes = (IsAuthenticated,)    
    # authentication_classes = (JWTAuthentication,)
    serializer_class = serializers.LoginUserSerializer

    def get(self, request):
        auth = get_authorization_header(request).split()
        print(auth)

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = UserSite.objects.filter(pk=id).first()
            return Response(serializers.LoginUserSerializer(user).data, status=HTTP_200_OK)
        raise AuthenticationFailed('unauthentication')


@extend_schema_view(
    post=extend_schema( 
        summary='Refresh token', tags=['User'], )
)
class RefreshJWTToken(APIView):
    """
    Refresh JWT token
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'accessToken': access_token
        })


@extend_schema_view(
    post=extend_schema(
        summary='Logout', tags=['User'] ),
) 
class LogoutUserView(APIView):
    """
    Logout User
    """
    permission_classes = (IsAuthenticated,)

    def post(self, _):
        response = Response()
        response.delete_cookie(key='refreshToken')
        response.data = {
            'message': 'user was logined'
        }
        return response












@extend_schema_view(
    post=extend_schema(
        request=serializers.ChangePasswordSerializer, 
        summary='Change Password', tags=['User']),
)
class ChangePasswordView(APIView):
    def post(self, request):
        user = request.user
        serializer = serializers.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)


   

#***********************************************************************************

def login_user(request):    
    if request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')
        try:
            user = UserSite.objects.get(username=username)
            if user is not None:
                user = authenticate(request, username=username, password=password)
                login(request, user)            
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))           
        except:
            messages.error(request, 'Enter a valid Username or Password') 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 




  
