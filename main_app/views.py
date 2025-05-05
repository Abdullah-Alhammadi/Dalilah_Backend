from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import City, Category, Place, Review
from .serializers import CitySerializer, CategorySerializer, PlaceSerializer, ReviewSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404


# Define the home view
class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to Dalilah!'}
        return Response(content)


class CityListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CategoryListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Places(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        city_id = request.query_params.get('city_id')
        category_id = request.query_params.get('category_id')
        queryset = Place.objects.filter(city_id=city_id, category_id=category_id)
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # ربط المكان بالمستخدم
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllPlacesView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, place_id):
        reviews = Review.objects.filter(place_id=place_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, place_id):
        data = request.data.copy()
        data['place'] = place_id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # ربط الريفيو بالمستخدم
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

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


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'All fields (username, email, password) are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)


class YourRecommendationsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)
