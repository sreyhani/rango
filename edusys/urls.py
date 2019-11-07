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
    path('profile/',profile,name = 'profile'),
]
