from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.shortcuts import render, redirect


# Create your views here.
def home(req):
    return render(req, "homepage.html")


def login_view(req):
    if req.POST:
        print(req)
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        print(req.user.is_authenticated)
        if user:
            login(req, user)
            return redirect('/')
        else:
            return render(req, 'login.html', {"error": False})
    return render(req, 'login.html', {"error": True})


def logout_view(req):
    logout(req)
    return redirect('/')
