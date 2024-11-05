from django.urls import path

from ..views.my_movies import my_movies

app_name = "app_my_movies"


urlpatterns = [
    path("", my_movies, name="my_movies"),
]
