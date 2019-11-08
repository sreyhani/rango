from django.contrib import admin

# Register your models here.
from edusys.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'first_day']


