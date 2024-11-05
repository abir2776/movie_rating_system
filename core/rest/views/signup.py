from django.shortcuts import render


def signup_user(request):
    return render(request, "app_login/signup.html", context={})
