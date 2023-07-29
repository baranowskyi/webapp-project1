from django.shortcuts import render
from users.models import UserSite 
from core.models import *

# from django.contrib.auth import get_user_model
#User = get_user_model()

# show artist all
def artist_all(request, slug_artist):
    return render(request, 'main.html') 

# show artist popular tracks
def artist_popular_tracks(request, slug_artist):
    return render(request, 'main.html') 

# show artist tracks
def artist_tracks(request, slug_artist):
    return render(request, 'main.html') 

# show artist albums
def artist_albums(request, slug_artist):
    return render(request, 'main.html')

# show artist playlists
def artist_playlists(request, slug_artist):
    return render(request, 'main.html')

# show artist reposts
def artist_reposts(request, slug_artist):
    return render(request, 'main.html')


