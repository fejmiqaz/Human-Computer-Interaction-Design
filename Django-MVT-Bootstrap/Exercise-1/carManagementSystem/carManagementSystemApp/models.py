
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    company_owner_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    TYPE_CHOICES = [
        ("S","Sedan"),
        ("H", "Hatchback"),
        ("C", "Coupe"),
        ("L", "Liftback")
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    horsepower = models.FloatField(default=0)
    max_speed = models.IntegerField(default=0)
    color = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.type}'
