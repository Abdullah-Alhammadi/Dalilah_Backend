from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import City, Category, Place, Review
from .serializers import CitySerializer, CategorySerializer, PlaceSerializer, ReviewSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404




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
    




class AllPlacesView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer






class PlaceDetailView(APIView):
    def get(self, request, place_id):
        place = get_object_or_404(Place, id=place_id)
        serializer = PlaceSerializer(place)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, place_id):
        place = get_object_or_404(Place, id=place_id)
        serializer = PlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, place_id):
        place = get_object_or_404(Place, id=place_id)
        place.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)






class ReviewListCreateAPIView(APIView):
    def get(self, request, place_id):
        reviews = Review.objects.filter(place_id=place_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, place_id):
        data = request.data.copy()
        data['place'] = place_id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class ReviewDetailAPIView(APIView):
    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)