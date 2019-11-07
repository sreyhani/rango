from django.urls import path

from edusys import views
from edusys.views import home, login_view, logout_view

urlpatterns = [
    path('', home),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
