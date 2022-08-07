from django.shortcuts import render
from .models import Author, Film, Genre, FilmInstance

# Create your views here.

def index(request):
    num_films = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    
    available = FilmInstance.objects.filter(status__exact='a'). count()
    
    return render(                     # contexto
        request,
        'index.html',
        context={
            'num_films': num_films,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_instances': num_instances,
            'available': available, 
        }
    )
