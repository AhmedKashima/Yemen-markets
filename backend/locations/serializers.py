from rest_framework import serializers
from .models import Governorate, City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name_ar', 'name_en', 'slug']

class GovernorateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    
    class Meta:
        model = Governorate
        fields = ['id', 'name_ar', 'name_en', 'slug', 'cities']
