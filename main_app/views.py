from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import City, Category, Place
from .serializers import CitySerializer, CategorySerializer, PlaceSerializer
from rest_framework import status

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to Dalilah!'}
    return Response(content)
  


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer




class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class Places(APIView):
    def get(self, request):
        city_id = request.query_params.get('city_id')
        category_id = request.query_params.get('category_id')
        queryset = Place.objects.filter(city_id=city_id, category_id=category_id)
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

