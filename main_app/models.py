from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='places')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Review(models.Model):
    content = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return self.content     


