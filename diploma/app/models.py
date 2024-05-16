from django.db import models
from django.contrib.auth.models import User

class UserMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()

def get_user_movies(user_id):
    user_movies = UserMovie.objects.filter(user_id=user_id)
    return user_movies
    