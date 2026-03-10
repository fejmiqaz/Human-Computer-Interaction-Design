from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    isActive = models.BooleanField()

    def __str__(self):
        return self.name

class GameStudio(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    yearFounded = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    game_studio = models.ForeignKey(GameStudio, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField()
    price = models.FloatField()
    number_of_copies = models.IntegerField()

    def __str__(self):
        return self.title