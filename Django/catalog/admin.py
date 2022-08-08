from django.contrib import admin
from .models import Author, Film, Genre, FilmInstance

# Register your models here.

admin.site.register(Author)
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(FilmInstance)
