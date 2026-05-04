from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.

def display(request):

    cakes = Cake.objects.all()

    data = {
        "cakes": cakes
    }

    return render(request, 'display.html', context=data)

def add_form(request):
    if request.method == 'POST':
        form = CakeAddForm(request.POST, request.FILES)

        if form.is_valid():
            cake = form.save(commit=False)
            cake.baker = Baker.objects.filter(user=request.user).first()
            cake.save()

            return redirect('display')

    form = CakeAddForm()

    return render(request, 'add.html',{'form':form})