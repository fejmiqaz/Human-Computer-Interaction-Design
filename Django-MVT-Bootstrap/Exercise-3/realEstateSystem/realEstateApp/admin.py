from datetime import datetime

from django.contrib import admin
from .models import *


# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'linkedin_link', ]

    # Agents and Features can only be added by superusers.
    def has_add_permission(self, request):
        return request.user.is_superuser


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

    # Agents and Features can only be added by superusers.
    def has_add_permission(self, request):
        return request.user.is_superuser


class PAInline(admin.StackedInline):
    model = PropertyAgent
    extra = 0


class PFInline(admin.StackedInline):
    model = PropertyFeature
    extra = 0


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'description']
    inlines = [PAInline, PFInline]

    # Sale listings can only be added by agents, and the agent who adds the listing is automatically assigned as one of the responsible agents for that property.
    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists() or request.user.is_superuser

    # A listing can only be deleted if no features have been added to describe it.
    def has_delete_permission(self, request, obj=None):
        return obj and not PropertyFeature.objects.filter(property=obj).exists()

    # Listings can only be modified by agents responsible for selling them, while other agents can only view those listings.
    def has_change_permission(self, request, obj=None):
        if obj:
            agent = PropertyAgent.objects.filter(property=obj).first()
            if agent:
                agent = agent.agent
                return request.user == agent.user
        return False

    # Superusers in the Admin panel see only the listings published on the current date.
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Property.objects.filter(date=datetime.today())

    # Save the model
    def save_model(self, request, obj, form, change):
        return super(PropertyAdmin, self).save_model(request, obj, form, change)

admin.site.register(Property, PropertyAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Agent, AgentAdmin)