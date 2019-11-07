from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


# Create your views here.
def home(req):
    return render(req, "homepage.html")


def signup(req: HttpRequest):
    if req.method == "POST":
        data = req.POST
        print(data)
        user = User(username=data.get('username'),first_name=data.get('first_name'),last_name=data.get('last_name'),password=data.get('password1')[0],email=data.get('email'))
        user.save()
        return redirect('/')
    else:
        return render(req, "signup.html", context={})
