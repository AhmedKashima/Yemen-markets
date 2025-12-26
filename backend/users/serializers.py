from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'full_name', 'avatar', 'city', 'is_verified']
        read_only_fields = ['is_verified']
