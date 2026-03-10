from django.contrib import admin
from .models import Category, Game, GameStudio
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "isActive")

@admin.register(GameStudio)
class GameStudioAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "yearFounded")

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "game_studio", "category", "user")