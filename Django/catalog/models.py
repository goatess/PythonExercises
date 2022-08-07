import uuid
from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=64,help_text='Pon el nombre del género')
    
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField('Title', max_length=64, help_text='Pon el nombre de la película')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField('Summary', max_length=100, help_text='Pon el argumento de la película')
    isbn = models.CharField('ISBN', max_legth=13, help_text= 'Pon aquí el ISBN de 13 caracteres')
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
class FilmInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID Único para esta película')
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    
class Author(models.Model):
    name = models.CharField(max_length=64,hel_text='Pon el nombre del autor')
    
    def __str__(self):
        return self.name