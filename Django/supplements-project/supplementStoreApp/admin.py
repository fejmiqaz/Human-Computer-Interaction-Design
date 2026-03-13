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

    # Automatically assign the user according to creation.
    exclude = ["user"]
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)