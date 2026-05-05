from django.contrib import admin
from django.contrib.auth import user_logged_in

from .models import *
# Register your models here.

class BouquetAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']
    exclude = ['user']

    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BouquetAdmin,self).save_model(request, obj, form, change)

class FlowerShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']

    def has_add_permission(self, request):
        return request.user.is_superuser

admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(FlowerShop, FlowerShopAdmin)