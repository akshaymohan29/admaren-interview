from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password']


# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         username = attrs.get('username')
#         password = attrs.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 message = 'Unable to log in with provided credentials.'
#                 raise serializers.ValidationError(message)
#         else:
#             message = 'Must include "username" and "password".'
#             raise serializers.ValidationError(message)

#         # attrs['user'] = user
#         return user