from django.urls import path
from core.api import views

urlpatterns = [
    path('api/track/like/show-likes/<int:track_id>', views.ShowLikesTrack.as_view(), name='show_likes_track'),    
    path('api/track/like/edit-like/<int:track_id>', views.EditLikeTrack.as_view(), name='edit_like_track'),  
    path('api/<slug:slug_artist>/show-tracks/', views.ArtistTracks.as_view(), name='show_artist_tracks'),    
]

