from django.urls import path

from . import views

app_name = "movies"

urlpatterns = [
    path('', views.home, name="home"),
    path('list/', views.movieList.as_view(), name="list"),
    path('create/', views.movieCreate, name="create"),
    path('<int:pk>/', views.movieDetail.as_view(), name="detail"),
    path('<int:pk>/update/', views.movieUpdate, name="update"),
    path('<int:pk>/delete/', views.movieDelete, name="delete"),
]