from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import City
from .serializers import CitySerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to Dalilah!'}
    return Response(content)
  




class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

