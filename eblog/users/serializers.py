from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError as DjangoValidationError


User = get_user_model()

class UserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user

# class CustomUserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def validate_username(self, value):
#         if User.objects.filter(username=value).exists():
#             raise serializers.ValidationError('Username already exists')
#         return value
#
#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError('Email already exists')
#         return value
#     def validate_password(self, value):
#         try:
#             validate_password(value)
#         except DjangoValidationError as e:
#             raise serializers.ValidationError(str(e))
#         return value
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user