from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    area = models.FloatField(default=0)
    date = models.DateField()
    picture = models.ImageField(upload_to='props/', null=True, blank=True)
    reserved = models.BooleanField(default = 0, null=True, blank=True)
    sold = models.BooleanField(default = 0)

    def __str__(self):
        return f'{self.name}'

class Agent(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(default=None)
    linkedin_link = models.URLField()
    num_completed_sales = models.IntegerField(default=0)
    email = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

class PropertyAgent(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.property} -- {self.agent}'

class Feature(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    value = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.value}'

class PropertyFeature(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.property} -- {self.feature}'