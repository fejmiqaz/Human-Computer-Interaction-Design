from django.contrib import admin
from django.db.models import Count

from .models import *

# Register your models here.

class CakeAdmin(admin.ModelAdmin):
    list_display = ['name',]

    # Cakes can only be modified by the bakers who added them, and other bakers can only see those cakes.
    def has_change_permission(self, request, obj = None):
        return obj and request.user == obj.baker.user

    def get_exclude(self, request, obj = None):

        if request.user.is_superuser:
            return []
        return ['baker']

    def save_model(self, request, obj, form, change):
        baker = Baker.objects.filter(user=request.user).first()

        cakes = Cake.objects.filter(baker=baker)

        # A baker can have a maximum of 10 cakes at a given time.
        if not change and len(cakes) > 10:
            return

        # A baker cannot add a cake if there is already a cake with the same name.
        if obj and Cake.objects.filter(name=obj.name).exists():
            return

        # The total price of the cakes of one baker must not exceed 10,000.

        sumOfPrice = 0

        for cake in cakes:
            sumOfPrice += cake.price

        if not change and sumOfPrice + obj.price > 10000:
            return

        obj.baker = baker

        super(CakeAdmin, self).save_model(request, obj, form, change)

class BakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    exclude = ['user']

     # Bakeries can only be deleted by super-users.
    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

    # Bakeries can only be added by super-users.
    def has_add_permission(self, request):
        return request.user.is_superuser

    # Bakeries can only be modified by super-users.
    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser

    # Bakeries with less than 5 cakes are shown to super-users in the Admin panel.
    def get_queryset(self, request):
        qs = super(BakerAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs.annotate(cakes_count=Count('cakes')).filter(cakes_count__lt=5)

        return qs

admin.site.register(Cake, CakeAdmin)
admin.site.register(Baker, BakerAdmin)

