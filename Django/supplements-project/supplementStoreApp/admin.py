from django.contrib import admin
from .models import Manufacturer,Category, Supplement

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "isActive")

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "type")

@admin.register(Supplement)
class SupplementAdmin(admin.ModelAdmin):
    list_display = ("name","description","category", "user", "photo", "price", "quantity")
