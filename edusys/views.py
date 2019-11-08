from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from edusys.forms import ContactUs, CourseForm, SearchCourse
from edusys.models import Course


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
                'testforwebelopers19@gmail.com',
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
    return render(req, "panel.html", context={'user': req.user})


@login_required(login_url='/login')
def setting(req):
    if req.method == 'POST':
        data = req.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if first_name != '':
            req.user.first_name = first_name
            req.user.save()
        if last_name != '':
            req.user.last_name = last_name
            req.user.save()
        return redirect('/profile')
    return render(req, "setting.html")


@user_passes_test(lambda u: u.is_superuser, login_url='/panel')
def create_new_course(req):
    if req.POST:
        form = CourseForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/courses')
    return render(req, "create_new_course.html", {"form": CourseForm})


def courses(req):
    # if req.POST:
    #     form = SearchCourse(req.POST)
    #     if form.is_valid():
    #         # department = form.cleaned_data.get("department")
    #         # teacher = form.cleaned_data.get("teacher")
    #         searched = form.cleaned_data.get("search_query")
    #         courses = Course.objects.filter(department=searched)
    #         # if department:
    #         #     courses = Course.objects.filter(department=searched)
    #         # elif teacher:
    #         #     courses = Course.objects.filter(teacher=searched)
    #         return render(req, "courses.html", {'courses': Course.objects.all(), 'searched': courses, 'form': form})
    form = SearchCourse()
    return render(req, "courses.html", {'courses': Course.objects.all(), 'form': form})
