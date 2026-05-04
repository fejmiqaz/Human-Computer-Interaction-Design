from django import forms

from .models import Cake


class CakeAddForm(forms.ModelForm):
    class Meta:
        model = Cake
        exclude = ['baker',]