from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Course(models.Model):
    user = models.ManyToManyField(User)
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=30)
    start_time = models.TimeField()
    exam_date = models.DateField(default="2000-1-1")
    end_time = models.TimeField()
    DAYS_OF_WEEK = [
        (0, 'شنبه'),
        (1, 'یکشنبه'),
        (2, 'دوشنبه'),
        (3, 'سه شنبه'),
        (4, 'چهارشنبه'),
    ]
    first_day = models.IntegerField(choices=DAYS_OF_WEEK)
    second_day = models.IntegerField(choices=DAYS_OF_WEEK, null=True, blank=True)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
#     def __init__(self,user = None):
#         self.user = user
