from rest_framework import serializers
from .models import City, Category, Place, Review

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'description']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']




class PlaceSerializer(serializers.ModelSerializer):
    city_name = serializers.StringRelatedField(source='city', read_only=True)
    category_name = serializers.StringRelatedField(source='category', read_only=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'description', 'location', 'city', 'category', 'city_name', 'category_name']





class ReviewSerializer(serializers.ModelSerializer):
    place_name = serializers.StringRelatedField(source='place', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'content', 'place', 'place_name'] 