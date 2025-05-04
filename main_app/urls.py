from django.urls import path
from .views import Home, CityListView, CategoryListView, Places, AllPlacesView, PlaceDetailView, ReviewListCreateAPIView, ReviewDetailAPIView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cities/', CityListView.as_view(), name='city-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('places/', Places.as_view(), name='places'),
    path('places/all/', AllPlacesView.as_view(), name='all-places'),
    path('places/<int:place_id>/', PlaceDetailView.as_view(), name='place-detail'),
    path('places/<int:place_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:review_id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
