from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class Genre(models.Model):
    name = models.CharField('Genre', max_length=64,help_text='Género de la película')

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField('Title', max_length=64, help_text='Nombre de la película')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField('Summary', max_length=100, help_text='Argumento breve de la película')
    isbn = models.CharField('ISBN', max_length=13, help_text='ISBN de 13 caracteres')
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

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad de la película')

class Meta:
    ordering = ['due_back']
    
    def __str__(self):
        return '%s (%s)' % (self.id, self.film.title)

class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text='Nombre del autor')
    last_name = models.CharField(max_length=100, help_text='Apellido del autor')
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

