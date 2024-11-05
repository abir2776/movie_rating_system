from django.urls import path

from ..views.login import login_user

app_name = "app_login"


urlpatterns = [
    path("", login_user, name="login"),
]
