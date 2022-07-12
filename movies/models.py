from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="avatars", default="no_profile.png")


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rotten_tomatoes = models.FloatField(default=0)
    metacritic = models.FloatField(default=0)
    imdb = models.FloatField(default=0)
    fandango = models.FloatField(default=0)
    flyer = models.ImageField(upload_to="flyers", default="no_flyer.png")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
