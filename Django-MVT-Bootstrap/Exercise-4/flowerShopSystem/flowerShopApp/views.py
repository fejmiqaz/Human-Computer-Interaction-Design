from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    bouquets = Bouquet.objects.all()

    return render(request, 'index.html', {'bouquets':bouquets})

def display(request ,id):
    bouquet = Bouquet.objects.filter(id=id).first()

    return render(request, 'display.html', {'bouquet': bouquet})