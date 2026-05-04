from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    properties = Property.objects.all()
    prop_list = []

    for p in properties:
        features = PropertyFeature.objects.filter(property=p)
        price = 0

        for f in features:
            price += f.feature.value

        prop_list.append(
            {
                'id':p.id,
                'name':p.name,
                'description':p.description,
                'area': p.area,
                'price': price,
                'picture': p.picture
            }
        )

    return render(request, 'index.html', {'properties':prop_list})

def edit(request, id):
    instance = Property.objects.filter(id=id).first()

    if request.method == 'POST':
        form = PropertyForm(request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = PropertyForm(instance=instance)

    return render(request, 'edit.html', {'form': form, 'property':instance})