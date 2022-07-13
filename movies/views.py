from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Movie
from .forms import MovieForm

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


class movieDetail(DetailView):
    model = Movie
    template_name = "movieDetail.html"
    context_object_name = "movie"

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