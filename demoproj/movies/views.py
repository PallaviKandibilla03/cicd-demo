from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

def show(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/show.html', {'movie': movie})
