from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Translator(models.Model):
    name = models.CharField(max_length=200, unique=True)
    nationality = models.CharField(max_length=200, unique=True)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.nationality})"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books', blank=True)
    translators = models.ManyToManyField(Translator, related_name='books', blank=True)

    publication_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='added_books')

    pages = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book} - {self.user} ({self.rating}"