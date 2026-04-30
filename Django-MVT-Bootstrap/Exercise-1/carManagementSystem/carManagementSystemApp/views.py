from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.

def homepage(request):
    cars = Car.objects.all()

    data = {
        'cars': cars
    }

    return render(request, 'homepage.html', context=data)

def add_car(request):
    if request.method == 'POST':
        form = CarAddForm(request.POST, request.FILES)

        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()

        return redirect('homepage')
    else:
        form = CarAddForm()
        data = {
            'form': form
        }
        return render(request, 'add-car.html', context=data)

def details(request,id):
    car = Car.objects.filter(id=id).first()

    if not car:
        return redirect('homepage')

    return render(request, "details.html", {"car":car})