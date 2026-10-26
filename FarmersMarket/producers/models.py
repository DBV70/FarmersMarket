from django.db import models
from django_countries.fields import CountryField

class Producer(models.Model):
    name = models.CharField(unique=True, max_length=100)
    address = models.CharField(max_length=200)
    country = CountryField()
    description = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    website = models.URLField(unique=True)
    image = models.ImageField(upload_to='media/producers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
