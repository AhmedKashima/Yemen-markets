from rest_framework import serializers
from .models import Ad
from locations.serializers import CitySerializer
from categories.serializers import CategorySerializer

class AdSerializer(serializers.ModelSerializer):
    city_detail = CitySerializer(source='city', read_only=True)
    category_detail = CategorySerializer(source='category', read_only=True)
    
    class Meta:
        model = Ad
        fields = '__all__'
        read_only_fields = ['owner', 'views', 'created_at'] # Removed 'status' from here so we can write to it internally

    def create(self, validated_data):
        # 1. Assign Owner
        validated_data['owner'] = self.context['request'].user
        
        # 2. FORCE ACTIVE STATUS (Auto-approve)
        validated_data['status'] = 'active' 
        
        return super().create(validated_data)