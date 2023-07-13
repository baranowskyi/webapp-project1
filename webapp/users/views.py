from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from users import serializers
from users.models import UserSite


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


@extend_schema_view(
    post=extend_schema(summary='Registration', tags=['Registration']),
)
class RegistrationView(CreateAPIView):
    queryset = UserSite.objects.all()
    serializer_class = serializers.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(
        request=serializers.ChangePasswordSerializer, 
        summary='Change Password', tags=['Registration']),
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


@extend_schema_view(
    get=extend_schema(summary='Profile', tags=['Users']),
    put=extend_schema(summary='Edit Profile', tags=['Users']),
    patch=extend_schema(summary='Edit Small', tags=['Users']),    
)
class MeView(RetrieveUpdateAPIView):
    queryset = UserSite.objects.all()
    serializer_class = serializers.MeSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return serializers.MeUpdateSerializer
        return serializers.MeSerializer
    
    def get_object(self):
        return self.request.user
    

#***********************************************************************************


def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()        
        password = request.POST.get('password')
        try:
            user = UserSite.objects.get(username=username)            
        except:
            messages.error(request, 'Not that User')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('profile')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # redirect on curent page
        else:
            messages.error(request, 'Wrong Username or Password')    
    return render(request, 'modal-login-form.html', {'page': page})     



def logout_user(request):
    logout(request)    
    # return redirect('profile')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # redirect on curent page    
    

############### registration form

class CustomRegisterForm(UserCreationForm):
	class Meta:
		model = UserSite
		fields = ("username", "email", "password1", "password2")
                

def register_user(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)         
            user.username = user.username.lower()
            user.save() 
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile') 
        else:
             messages.error(request, 'Error Registration')
    form = CustomRegisterForm()    
    return render(request, 'modal-registration-form.html', {'form': form})
    
