from django.urls import path

from ..views.home import home

app_name = "app_home"


urlpatterns = [
    path("", home, name="home"),
]
