from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from django.contrib.auth import authenticate

from users.models import UserSite


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Create User
    """
    class Meta:
        model = UserSite
        fields = ['id', 'username', 'password', 'email',]
        extra_kwargs = {
            'password': { 'write_only': True }
        }

    def validate_email(self, value):
        email = value.lower()
        if UserSite.objects.filter(email=email).exists():
            raise ParseError(
                "Email is exists in database"
            )
        return email    
    
    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save() 
        return instance
    
        
    
class LoginUserSerializer(serializers.ModelSerializer):
    """
    Login User
    """  
    class Meta:
        model = UserSite
        fields = ['id', 'username', 'password', 'email',]
        extra_kwargs = {
            'password': { 'write_only': True },
            'username': { 'read_only': True }
        }
























class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserSite
        fields = (             
            'username',
            'password',            
        )

    def validate(self, data):        
        username = data.get('username', None)
        password = data.get('password', None)
        if username and password:            
            user = authenticate(username=username, password=password)
            if user is None:                
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
            if not user.is_active:
                msg = 'User not activate.'
                raise serializers.ValidationError(msg, code='authorization')            
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')  
        data['user'] = user
        return data             
    
                     
# ////////////////////////////////////////////////////////////////////////////////////////////////
        
        


    
    

class ChangePasswordSerializer(serializers.ModelSerializer):
    
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserSite
        fields = (
            'old_password', 
            'new_password',
            )
    
    def validate(self, data):
        user = self.instance
        old_password = data.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Wrong Password'
            )
        return data
    
    def validate_new_password(self, value):
        validate_password(value)
        return value
        
    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance
 