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
from edusys.models import Course, UserProfile


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
        profile = UserProfile()
        user.userprofile = profile
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
        image = req.FILES.get('image')
        if image:
            req.user.userprofile.avatar = image
            req.user.userprofile.save()
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
    my_courses = req.user.course_set.all()
    all_courses = Course.objects.all()
    for course in my_courses:
        all_courses = all_courses.exclude(id=course.id)
    if req.POST:
        form = SearchCourse(req.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            department = form.cleaned_data.get('department')
            teacher = form.cleaned_data.get("teacher")
            searched = form.cleaned_data.get("search_query")
            searched_courses = None
            department_search_result = None
            name_search_result = None
            teacher_name_resoult = None
            if (not department) and (not name) and (not teacher):
                searched_courses = Course.objects.filter(department = searched)
            else:
                if department:
                    department_search_result = Course.objects.filter(department=searched)
                if name:
                    name_search_result = Course.objects.filter(name=searched)
                if teacher:
                    teacher_name_resoult =  Course.objects.filter(teacher=searched)
            return render(req, "courses.html", {'courses': all_courses, 'form': form, 'my_courses': my_courses,
                                                'searched': searched_courses,'dep_searched':department_search_result,'name_searched':name_search_result,'teacher_searched':teacher_name_resoult})
    form = SearchCourse()

    return render(req, "courses.html", {'courses': all_courses, 'form': form, 'my_courses': my_courses, })


def get_course(req, course_id):
    course = Course.objects.filter(id=course_id).all()[0]
    course.user.add(req.user)
    course.save()
    return redirect('/courses')


def remove_course(req, course_id):
    course = Course.objects.filter(id=course_id).all()[0]
    course.user.remove(req.user)
    course.save()
    return redirect('/courses')


def course_page(req,course_id):
    course = Course.objects.filter(id=course_id).all()[0]
    return render(req,"course_page.html",{'course':course})
