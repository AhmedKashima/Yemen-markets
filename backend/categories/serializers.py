from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name_ar', 'name_en', 'slug', 'icon', 'children']

    def get_children(self, obj):
        serializer = CategorySerializer(obj.children.all(), many=True)
        return serializer.data
