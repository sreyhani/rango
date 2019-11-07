from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from edusys.forms import ContactUs


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


def signup(req: HttpRequest):
    user_exists = 'نام کاربری شما در سیستم موجود است'
    password_not_match = 'گذرواژه و تکرار گذرواژه یکسان نیستند'
    if req.method == "POST":
        data = req.POST
        print(data)
        print(data.get('first_name'))
        my_user_name = data.get('username')
        pass1 = data.get('password1')
        pass2 = data.get('password2')
        if User.objects.filter(username=my_user_name).count() != 0:
            return render(req, "signup.html", context={'error': user_exists})
        if pass1 != pass2:
            return render(req, "signup.html", context={'error': password_not_match})
        user = User(username=my_user_name, first_name=data.get('first_name'), last_name=data.get('last_name'),
                    email=data.get('email'))
        user.set_password(pass1)
        user.save()
        return redirect('/')
    else:
        return render(req, "signup.html", context={})


def contact_us(req):
    if req.method == 'POST':
        form = ContactUs(req.POST)
        if form.is_valid():
            clean = form.cleaned_data
            recipient_list = ['webe19lopers@gmail.com']
            title = clean.get('title')
            text = clean.get('text') + '\n' + clean.get('email')

            send_mail(
                title,
                text,
                '',
                ['webe19lopers@gmail.com'],
                fail_silently=False,
            )
            return render(req, 'blank.html')
    form = ContactUs()
    return render(req, 'contact_us.html', {'done': False, 'form': form})


@login_required(login_url='/login')
def profile(req):
    return render(req, "profile.html", context={'user': req.user})


@login_required(login_url='/login')
def panel(req):
    return render(req, "panel.html")
