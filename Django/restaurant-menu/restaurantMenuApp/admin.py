from django.contrib import admin

from .models import Category, Company, MenuItem
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "date_of_partnership")
    list_per_page = 5

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_or_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.user == request.user

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(CompanyAdmin, self).save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "isActive")

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_or_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.user == request.user

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "supplier", "description", "user", "food_image", "price", "quantity", "category")
    list_filter = ("category", "quantity")
    list_editable = ("price", "quantity", "category")
    search_fields = ("name", "description")
    ordering = ("name",)
    list_per_page = 20

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

    def has_view_or_change_permission(self, request, obj = None):
        if obj is None:
            return True
        return obj.user == request.user

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MenuItemAdmin, self).save_model(request,obj, form, change)

    def get_queryset(self, request):
        return MenuItem.objects.filter(user=request.user)