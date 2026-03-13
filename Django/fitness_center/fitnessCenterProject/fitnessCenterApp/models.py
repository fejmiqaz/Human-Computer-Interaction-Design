from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    CHOICES = [
        ("Cardio", "cardio"),
        ("Yoga", "yoga"),
        ("Strength", "strength")
    ]
    name = models.CharField(max_length=100, choices=CHOICES)
    description = models.TextField()
    isDemanded = models.BooleanField()

    def __str__(self):
        return self.name

class Instructor(models.Model):

    CHOICES = [
        ("Starter", "starter"),
        ("Certified", "certified"),
        ("Professional Trainer", "professional-trainer")
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    biography = models.TextField()
    level = models.CharField(max_length=100, choices=CHOICES)

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.FloatField()
    num_free_spots = models.IntegerField()

    def __str__(self):
        return self.name