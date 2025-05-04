from django.contrib import admin

# Register your models here.
from .models import City, Category, Place, Review

admin.site.register(City)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Review)
