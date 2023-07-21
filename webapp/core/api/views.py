from core.api.serializers import *
from core.models import Like, Track

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from core.permissions import IsOwnerOrReadOnly, ReadOnly

from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth.decorators import login_required


#---------------------------------------- LIKES TRACK --------------------------------------------


@extend_schema_view(
    get=extend_schema(summary='Who Likes Track', tags=['Like Track']),    
)
class WhoLikesTrack(ListAPIView):

    serializer_class = WhoLikesSerializer     
    permission_classes = (IsAuthenticatedOrReadOnly,)   

    def get_queryset(self):
        queryset = Like.objects.filter(track=self.kwargs['track_id'])     
        if queryset:            
            return queryset
        raise ParseError(
                "Track not exists likes"
            )   
       
  


@extend_schema_view(
    post=extend_schema(summary='Add Like Track', tags=['Like Track']), 
    delete=extend_schema(summary='Delete Like Track', tags=['Like Track']),   
)
class AddLikeTrack(ListAPIView, CreateAPIView, DestroyAPIView):

    serializer_class = AddLikeSerializer  
    # authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, ) 
    lookup_field = 'track_id'     

    def get_queryset(self):   
        queryset = Like.objects.filter(track=self.kwargs['track_id'], artist=self.request.user.artist)           
        if queryset:
            return queryset
        raise ParseError(
                "Track not exists likes"    
            )  

    def perform_create(self, serializer): 
        if Like.objects.filter(track=self.kwargs['track_id'], artist=self.request.user.artist).exists():      
            raise ParseError(
                    "You like track"    
                )  
        serializer.save(artist=self.request.user.artist, track=Track.objects.get(id=self.kwargs['track_id']))
      

    


