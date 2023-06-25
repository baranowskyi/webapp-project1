from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from users.models import UserSite

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UserSite
        fields = (
            'id',
            'username',
            'password',
            'email',
        )

    def validate_email(self, value):
        email = value.lower()
        if UserSite.objects.filter(email=email).exists():
            raise ParseError(
                "email exists"
            )
        return email
    
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = UserSite.objects.create_user(**validated_data)
        return user
    
    # def create(self, validated_data):
    #     profile_data = validated_data.pop('username')
    #     user = User.objects.create(**validated_data)
    #     User.objects.create(user=user, **profile_data)
    #     return user   
        
    

class ChangePasswordSerializer(serializers.ModelSerializer):
    
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserSite
        fields = ('old_password', 'new_password')
    
    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Wrong Password'
            )
        return attrs
    
    def validate_new_password(self, value):
        validate_password(value)
        return value
        
    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class MeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSite
        fields = {
            'id',
            'username',
            'email',
        }
        

class MeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSite
        fields = '__all__'