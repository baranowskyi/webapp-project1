from django.shortcuts import render
from users.models import UserSite 
from core.models import *

# from django.contrib.auth import get_user_model
#User = get_user_model()

def main_page(request):
    return render(request, 'index.html')


# show profile page
def profile(request, slug_artist):     
    artist_info = Artist.objects.filter(slug_artist=slug_artist).select_related('username').values(
        'display_name',        
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
    context = {
         'artist_info': artist_info,
    } 
    if request.user.is_authenticated: 
        active_user = request.user.username # get active user
        id_user = UserSite.objects.filter(username=active_user).values('id')[0]['id'] # get id active user   
        active_artist_info = Artist.objects.filter(username=id_user).values(
            'profile_url',
            'avatar_image',
        )  
        context_active_user = {
            'active_artist_info': active_artist_info,
        }  
        context.update(context_active_user)
       
    return render(request, 'main.html', context)
