from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Baker(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(default='/images/person.png')

    def __str__(self):
        return f'{self.name} - {self.surname}'

class Cake(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    description = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField()
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE, null=True, blank=True, related_name='cakes')

    def __str__(self):
        return f'{self.name}'
