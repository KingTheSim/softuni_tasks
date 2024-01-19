from django.db import models


class CustomManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(num_movies=models.Count('director_movie')).order_by('-num_movies', 'full_name')

