from django.urls import path
from .views import Home, CityListView, CategoryListView, Places, AllPlacesView, PlaceDetailView, ReviewListCreateAPIView, ReviewDetailAPIView, CreateUserView, LoginView, VerifyUserView, YourRecommendationsView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cities/', CityListView.as_view(), name='city-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('places/', Places.as_view(), name='places'),
    path('places/all/', AllPlacesView.as_view(), name='all-places'),
    path('places/<int:place_id>/', PlaceDetailView.as_view(), name='place-detail'),
    path('places/<int:place_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:review_id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('users/verify/', VerifyUserView.as_view(), name='verify'),
    path('places/recommendations/', YourRecommendationsView.as_view(), name='your-recommendations'),

]
