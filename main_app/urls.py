from django.urls import path
from .views import Home, CityListView, CategoryListView, Places
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cities/', CityListView.as_view(), name='city-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('places/', Places.as_view(), name='places'),
]