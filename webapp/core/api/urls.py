from django.urls import path
from core.api import views

urlpatterns = [
    path('api/who-likes-track/<int:track_id>', views.WhoLikesTrack.as_view(), name='who_likes_track'),    
    path('api/add-like-track/<int:track_id>', views.AddLikeTrack.as_view(), name='add_like_track'),      
]

