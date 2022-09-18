from statistics import mode
from django.forms import ModelForm

from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = [
            "title",
            "year",
            "rotten_tomatoes",
            "metacritic",
            "imdb",
            "fandango",
            "flyer",
        ]