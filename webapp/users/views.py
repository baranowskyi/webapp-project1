from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from users import serializers
from users.models import UserSite
from users.forms import CustomRegisterForm


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


@extend_schema_view(
    post=extend_schema(summary='Registration', tags=['User']),
)
class RegistrationView(CreateAPIView):
    queryset = UserSite.objects.all()
    serializer_class = serializers.RegistrationSerializer


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
        username = request.POST.get('username').lower()        
        password = request.POST.get('password')
        try:
            user = UserSite.objects.get(username=username)
            if user is not None:
                user = authenticate(request, username=username, password=password)
                login(request, user)            
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # redirect on curent page           
        except:
            messages.error(request, 'Enter a valid Username or Password') 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # redirect on curent page


def logout_user(request):
    logout(request) 
    request.user = None
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # redirect on curent page    



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
    
