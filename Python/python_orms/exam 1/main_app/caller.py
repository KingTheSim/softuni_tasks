import os
import math

import django
from django.db import models

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create and run your queries within functions


def get_directors(search_name=None, search_nationality=None):
    if search_name and search_nationality:
        all_directors = Director.objects.filter(full_name__icontains=search_name,
                                                nationality__icontains=search_nationality).order_by('full_name')
    elif search_name:
        all_directors = Director.objects.filter(full_name__icontains=search_name).order_by('full_name')
    elif search_nationality:
        all_directors = Director.objects.filter(nationality__icontains=search_nationality).order_by('full_name')
    else:
        return ""

    return "\n".join(
        f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}" for d in
        all_directors)


def get_top_director():
    # return Director.filter(rating=self.aggregate(max_rating=models.Max('rating'))['max_rating']).first()
    all_directors = Director.objects.annotate(num_movies=models.Count('director_movie')).order_by('-num_movies', 'full_name').first()
    if all_directors:
        return f"Top Director: {all_directors.full_name}, movies: {all_directors.num_movies}."
    else:
        return ""


def get_top_actor():
    all_actor = Actor.objects.annotate(num_movies=models.Count('starring_actor_movie')).order_by('-num_movies', 'full_name').first()

    if all_actor:
        movies = all_actor.starring_actor_movie.all()
        if movies:
            movie_rating = sum(m.rating for m in movies) / len(movies)
            return f"Top Actor: {all_actor.full_name}, starring in movies: {', '.join(m.title for m in movies)}, movies average rating: {movie_rating:.1f}"
        else:
            return ""
    else:
        return ""
