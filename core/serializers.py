from djoser.serializers import UserSerializer as BaseSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        fields = ('id', 'username', 'email', 'first_name', 'last_name')