from django.urls import path

from edusys import views
from edusys.views import *

urlpatterns = [
    path('', home),
    path('signup/',signup),
]
