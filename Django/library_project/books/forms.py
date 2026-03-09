from django import forms

from Django.library_project.books.models import Book, Author, Genre, Translator, Rating


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title", "author", "genres", "translators", "publication_date",
            "pages", "cover", "is_available"
        ]
        widgets = {
            "publication_date": forms.DateInput(attrs={"type": "date"}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [ "rating", "comment"]

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [ "genre", "description"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]

class TranslatorForm(forms.ModelForm):
    class Meta:
        model = Translator
        fields = ["name", "nationality", "birthdate"]
        widgets = { "birthdate": forms.DateInput(attrs={"type": "date"}) }