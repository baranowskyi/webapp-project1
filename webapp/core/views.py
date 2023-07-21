from django.shortcuts import render
from users.models import UserSite 
from core.models import *

# from django.contrib.auth import get_user_model
#User = get_user_model()


def main_page(request):
    return render(request, 'index.html')


# show profile page
def profile(request, slug_artist): 
    # get artist info    
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

        'username__id',
        'username__username',
        'username__pro_user',              
        ) 
    
    # get artist track
    artist_track = Artist.objects.filter(slug_artist=slug_artist).select_related('track').values(
        'track__id',
        'track__title',
        'track__slug_track',        
        'track__track_file',
        'track__cover_image',  
        'track__genre',
        # 'track__tag',
        'track__public_access',      
        'track__publish_date',
        # 'track__update_date',
        # 'track__discription',
        'track__copy_link',
        'track__download_access',
        'track__buy_link',
        'track__play_counter',
        'track__like_counter',
        'track__repost_counter',
        'track__comment_counter',        
    ).order_by('-track__publish_date')

    context = {
        'artist_info': list(artist_info),
        'artist_track': list(artist_track),
    }
    
    # get active artist info if he authenticated
    if request.user.is_authenticated: 
        active_user = request.user.username # get active user
        id_user = UserSite.objects.filter(username=active_user).values('id')[0]['id'] # get id active user   
        active_artist_info = Artist.objects.filter(username=id_user).values(
            'profile_url',
            'avatar_image',
            'username__username',            
        ) 
        context_active_artist = {
            'active_artist_info': list(active_artist_info),
        }
        context.update(context_active_artist) # update context data       

    return render(request, 'main.html', context) 

