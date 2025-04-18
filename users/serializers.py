from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user

class UserLoginSerializer(serializers.Serializer):
    email =  serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise serializers.ValidationError('Invalid login credentials')
            
        else:
            raise serializers.ValidationError('Must include email and password')
        
        data['user'] = user
        return data

class UserLogoutSerializer(serializers.Serializer):
    pass

class ProfileSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'