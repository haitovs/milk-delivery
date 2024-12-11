from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'phone_number', 'address']

    def create(self, validated_data):
        # Hash the password using create_user
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'name', 'phone_number', 'address', 'created_at']
        read_only_fields = ['email', 'created_at']
