from django.db import models


# Create your models here.
class Course(models.Model):
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=30)
    time_choices = ['0', '1', '2', '3', '4']
    start_time = models.DateTimeField()
    end_time = models.IntegerField(max_length=30)
    first_day = models.CharField(max_length=1, choices=time_choices)
    end_day = models.IntegerField(max_length=30)
