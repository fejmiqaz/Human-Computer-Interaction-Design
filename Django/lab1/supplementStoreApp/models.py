from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    isActive = models.BooleanField()

class Manufacturer(models.Model):

    class ManufacturerType(models.TextChoices):
        SMALL = 'S', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'

    name = models.CharField(max_length=100)
    date = models.DateField()
    type = models.CharField(max_length=1, choices=ManufacturerType.choices, default=ManufacturerType.SMALL)

class Supplement(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField()
    price = models.FloatField()
    quantity = models.IntegerField()
