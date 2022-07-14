from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Movie
from .forms import MovieForm
from .utils import get_chart

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create your views here.
def home(request):
    hello = "Hello World"
    context = {
        "hello": hello
    }
    return render(request, "home.html", context)


class movieList(ListView):
    model = Movie
    template_name = "movieList.html"
    context_object_name = "movies"


def movieDetail(request, pk):
    movie_qs = Movie.objects.all()
    movie = Movie.objects.get(id=pk)
    movie_df = pd.DataFrame(movie_qs.values())
    temp = movie_df["title"] == movie.title
    movie_df = movie_df[temp]
    chart = get_chart(movie_df)
    movie_df = movie_df.to_html()
    context = {
        "movie": movie,
        "movie_df": movie_df,
        "chart": chart
    }
    return render(request, "movieDetail.html", context)

def movieCreate(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/list")
    context = {
        "form": form
    }
    return render(request, "movieCreate.html", context)

def movieUpdate(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect("/list")
    context = {
        "form": form,
        "movie": movie
    }
    return render(request, "movieUpdate.html", context)

def movieDelete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect("/")