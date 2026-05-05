import datetime
from random import choices

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Bouquet(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    BOUQUET_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    ]
    size = models.CharField(max_length=6, choices=BOUQUET_SIZES, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='pics/', null=True, blank=True)
    price = models.FloatField(default=0)
    year = models.IntegerField(default=2000)
    isFresh = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.name} - {self.year}'

class FlowerShop(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(default = datetime.date.today())
    isEU = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.name} - {self.location}'

