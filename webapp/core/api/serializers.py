from rest_framework import serializers
from core.models import Like
from users.models import UserSite
from core.models import Artist, Track

class UserSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSite
        fields = ['id', 'username', ]


class WhoLikesSerializer(serializers.ModelSerializer): 
    
    artist = serializers.StringRelatedField(many=False)
    track = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Like
        fields = ['artist', 'track',]        
    
       
class AddLikeSerializer(serializers.ModelSerializer): 
    
    track = serializers.ReadOnlyField(source='track.title')
    artist = serializers.ReadOnlyField(source='artist.display_name')    
       
    class Meta:
        model = Like
        fields = ['track', 'artist', ] 
         
              