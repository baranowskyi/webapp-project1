from django.urls import path
from . import views

urlpatterns = [   
    path('<slug:slug_artist>', views.artist_all, name='artist_all'),   
    path('<slug:slug_artist>/popular-tracks', views.artist_popular_tracks, name='artist_popular_tracks'),    
    path('<slug:slug_artist>/tracks', views.artist_tracks, name='artist_tracks'), 
    path('<slug:slug_artist>/albums', views.artist_albums, name='artist_albums'), 
    path('<slug:slug_artist>/sets', views.artist_playlists, name='artist_playlists'), 
    path('<slug:slug_artist>/reposts', views.artist_reposts, name='artist_reposts'), 
     
]

