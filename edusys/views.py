from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


# Create your views here.
def home(req):
    return render(req, "homepage.html")

def signup(req: HttpRequest):
    user_exists='نام کاربری شما در سیستم موجود است'
    password_not_match = 'گذرواژه و تکرار گذرواژه یکسان نیستند'
    if req.method == "POST":
        data = req.POST
        print(data)
        print(data.get('first_name'))
        user_name = data.get('username')
        pass1 = data.get('password1')
        pass2 = data.get('password2')
        # if User.objects.filter().count() != 0:
        #     return render(req,"signup.html",context={'error':user_exists})
        # if pass1 != pass2:
        #     return render(req,"signup.html",context={'error':password_not_match})
        user = User(username=user_name, first_name=data.get('first_name'), last_name=data.get('last_name'), email=data.get('email'))
        user.set_password(pass1)
        user.save()
        return redirect('/')
    else:
        return render(req, "signup.html", context={'error':''})
