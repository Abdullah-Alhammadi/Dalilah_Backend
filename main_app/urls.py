from django.urls import path
from .views import Home, CityListView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cities/', CityListView.as_view(), name='city-list'),
]