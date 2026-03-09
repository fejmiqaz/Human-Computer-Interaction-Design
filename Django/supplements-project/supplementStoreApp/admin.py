from django.contrib import admin
from .models import Manufacturer,Category, Supplement

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Supplement)
