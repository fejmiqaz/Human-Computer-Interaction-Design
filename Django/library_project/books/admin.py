from django.contrib import admin

from .models import Book, Author, Translator, Rating, Genre

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(Rating)
admin.site.register(Genre)