from rest_framework import serializers
from .models import City, Category, Place, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


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
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'description', 'location',
            'city', 'category',
            'city_name', 'category_name',
            'username', 'user'
        ]
        extra_kwargs = {
            'user': {'read_only': True}
        }


class ReviewSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


