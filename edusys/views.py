from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req, "homepage.html")
def register(req):
    return render(req,"")