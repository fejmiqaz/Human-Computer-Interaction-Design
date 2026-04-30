from django.contrib import admin
from .models import *

# Admin Panel Functionalities

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    # Cars are displayed in the admin panel by their name and type.
    list_display = ['name', 'type']
    exclude= ['user']
    # The admin panel includes filtering options by car type, allowing easier navigation and management of vehicles.
    list_filter = ["type"]

    # When a new car is added, the logged-in user is automatically assigned as its owner.
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(CarAdmin, self).save_model(request, obj, form, change)

    # Only the user who added the car or a superuser can delete it, preventing unauthorized deletions.
    def has_delete_permission(self, request, obj = None):
        if obj is None:
            return True
        return request.user.is_superuser or request.user == obj.user

class ManufacturerAdmin(admin.ModelAdmin):
    # Manufacturers are displayed by their name and owner in the admin panel.
    list_display = ["name", "company_owner_name"]

    # Manufacturers can only be added or deleted by superusers, as they represent shared data across all users.
    def has_add_permission(self, request):
        return request.user.is_superuser

    # Manufacturers can only be added or deleted by superusers, as they represent shared data across all users.
    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

    #Regular users can only view manufacturers linked to the cars they own, ensuring access is restricted to relevant data.
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Manufacturer.objects.all()
        else:
            return Manufacturer.objects.filter(car__user=request.user).distinct()

admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)