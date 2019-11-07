from django.urls import path

from edusys import views
from edusys.views import home, login_view, logout_view
from edusys.views import *

urlpatterns = [
    path('', home),
<<<<<<< HEAD
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('signup/',signup),
=======
    path('signup/', signup, name='signup'),
>>>>>>> 87c7ad2d1f37ec770a2f3571302d78089beeb527
]
