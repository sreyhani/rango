from django.conf.urls import url
from django.urls import path

from edusys import views
from edusys.views import home, login_view, logout_view
from edusys.views import *

urlpatterns = [
    path('', home),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('contact_us/', contact_us, name='contact_us'),
    path('profile/', profile, name='profile'),
    path('panel/', panel, name='panel'),
    path('setting/', setting, name='setting'),
    path('create_new_course/', create_new_course, name='create_new_course'),
    path('courses/', courses, name='course'),
    url(r'get_course/(?P<course_id>[0-9]+)$', get_course, name='get_course'),
    url(r'remove_course/(?P<course_id>[0-9]+)$', remove_course, name='remove_course'),
    url(r'course_page/(?P<course_id>[0-9]+)$', course_page, name='course_page'),

]
