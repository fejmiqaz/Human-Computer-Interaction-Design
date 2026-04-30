from django import forms

from .models import *

class CarAddForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['user']