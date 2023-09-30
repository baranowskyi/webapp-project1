from core.api.serializers import *
from core.models import Like, Track

from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from core.permissions import IsOwnerOrReadOnly, ReadOnly

from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


#---------------------------------------- LIKES TRACK --------------------------------------------


@extend_schema_view(
    get=extend_schema(summary="Show track Likes", tags=["Track Likes"]),    
)
class ShowLikesTrack(ListAPIView):

    serializer_class = ShowLikesSerializer     
    permission_classes = (IsAuthenticatedOrReadOnly,)   

    def get_queryset(self):
        queryset = Like.objects.filter(track=self.kwargs['track_id'])     
        if queryset:            
            return queryset
        raise ParseError(
                "Track doesn't exist"
            ) 
    

@extend_schema_view(    
    post=extend_schema(summary='Add Like the track', tags=["Track Likes"]), 
    delete=extend_schema(summary='Delete Like from the track', tags=["Track Likes"]),   
)
class EditLikeTrack(CreateAPIView, DestroyAPIView):

    serializer_class = LikeSerializer  
    # authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, ) 
    lookup_field = 'track_id'     

    def get_queryset(self):   
        queryset = Like.objects.filter(track=self.kwargs['track_id'], artist=self.request.user.artist)           
        if queryset:
            return queryset
        raise ParseError(
                "Track doesn't has likes"    
            )  

    def perform_create(self, serializer): 
        if Like.objects.filter(track=self.kwargs['track_id'], artist=self.request.user.artist).exists():      
            raise ParseError(
                    "You like the track"    
                )  
        serializer.save(artist=self.request.user.artist, track=Track.objects.get(id=self.kwargs['track_id']))

      

#---------------------------------------- TRACK -------------------------------------------- 
   

@extend_schema_view(
    get=extend_schema(summary="Show Artist Tracks", tags=["Artist Tracks"]),    
)
class ArtistTracks(ListAPIView):

    serializer_class = ArtistTracksSerializer   
    permission_classes = (IsAuthenticatedOrReadOnly,)   

    def get_queryset(self):
        queryset = Track.objects.filter(artist__slug_artist=self.kwargs['slug_artist'])    
        if queryset:            
            return queryset
        raise ParseError(
                "Artist doesn't has tracks"
            )   
    

#---------------------------------------- ARTIST --------------------------------------------------

@extend_schema_view(
    get=extend_schema(summary="Show Artist Info", tags=["Artist Info"]),    
)
class ArtistInfo(ListAPIView):

    serializer_class = ArtistInfoSerializer   
    permission_classes = (IsAuthenticatedOrReadOnly,) 

    def get_queryset(self):
        queryset = Artist.objects.filter(slug_artist=self.kwargs['slug_artist'])    
        if queryset:            
            return queryset
        raise ParseError(
                "Artist doesn't exist"
            )  
    

@extend_schema_view(
    get=extend_schema(summary="Show Current Artist Info", tags=["Artist Info"]),    
)    
class CurrentArtistInfo(ListAPIView):

    serializer_class = ArtistInfoSerializer   
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Artist.objects.filter(username__id=self.request.user.id)
        print(self.request.user)
        if queryset:            
            return queryset
        raise ParseError(
                "Artist doesn't authenticate"
            )  