from django.contrib import admin
from .models import Category, Instructor, Training

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "isDemanded"]

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "biography", "level"]

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ["name", "instructor", "user", "description","image", "price"]

    # Automatically assign the user who created the Training.
    exclude = ["user"]
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)
