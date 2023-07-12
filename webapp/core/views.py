from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import UserSite 
from core import models
from users import serializers
from core.serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from core.permitions import *

# from django.contrib.auth import get_user_model
#User = get_user_model()

def main_page(request):
    return render(request, 'index.html')



def profile(request, slug_artist):
    artist_info = models.Artist.objects.filter(slug_artist=slug_artist).select_related('username').values(
        'display_name',
        # 'slug_artist',        
        'profile_url',
        'avatar_image',
        'header_image',
        'verification',
        'first_name',
        'last_name',
        'city',
        'country',
        'bio',  
        'follower_counter',
        'following_counter',
        'track_counter',
        'username__pro_user'       
        )      
    # print(artist_info)   
    context = {
         'artist_info': artist_info,        
    }    
    return render(request, 'main.html', context)


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
    