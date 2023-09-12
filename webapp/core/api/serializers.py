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


#------------------------ Artist info -----------------------------------------

class UserNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSite
        fields = ['username', 'pro_user',]


class ArtistInfoSerializer(serializers.ModelSerializer):
    username = UserNameSerializer(many=False, read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'


# stock serializer don't use
class CurrentArtistInfoSerializer(serializers.ModelSerializer):
    username = UserNameSerializer(many=False, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'display_name', 'avatar_image', 'username',]
        
        
        
   