from django.urls import path

from ..views.signup import signup_user

app_name = "app_signup"


urlpatterns = [
    path("", signup_user, name="signup"),
]
