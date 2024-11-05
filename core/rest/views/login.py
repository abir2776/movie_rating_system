from django.shortcuts import render


def login_user(request):
    return render(request, "app_login/login.html", context={})
