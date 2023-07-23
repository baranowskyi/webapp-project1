from rest_framework import serializers
from core.models import Like, Track, Artist
from users.models import UserSite



class ShowLikesSerializer(serializers.ModelSerializer):    
    artist = serializers.StringRelatedField(many=False)
    track = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Like
        fields = ['artist', 'track',] 

    
       
class LikeSerializer(serializers.ModelSerializer):    
    track = serializers.ReadOnlyField(source='track.title')
    artist = serializers.ReadOnlyField(source='artist.display_name')    
       
    class Meta:
        model = Like
        fields = ['artist', 'track', ] 


#------------------------ Artist tracks ---------------------------------


class NameArtistLikeSerializer(serializers.ModelSerializer):    
    artist = serializers.ReadOnlyField(source='artist.display_name')    
       
    class Meta:
        model = Like
        fields = ['artist', ]


class NameArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = ['id', 'display_name', ]
         
class ArtistTracksSerializer(serializers.ModelSerializer):
    likes = NameArtistLikeSerializer(many=True, read_only=True)
    artist = NameArtistSerializer(many=False, read_only=True)
    
    class Meta:
        model = Track
        fields = '__all__'