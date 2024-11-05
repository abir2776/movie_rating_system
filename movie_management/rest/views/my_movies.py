from django.shortcuts import render


def my_movies(request):
    return render(request, "app_movie/my_movies.html", context={})
