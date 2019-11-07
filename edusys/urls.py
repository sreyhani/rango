from django.urls import path

from edusys import views
from edusys.views import home

urlpatterns = [
    path('', home),
    path('register/',register),
]
