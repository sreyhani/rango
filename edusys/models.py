from django.db import models


# Create your models here.
class Course(models.Model):
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
    DAYS_OF_WEEK = [
        (0, 'شنبه'),
        (1, 'یکشنبه'),
        (2, 'دوشنبه'),
        (3, 'سه شنبه'),
        (4, 'چهارشنبه'),
    ]
    first_day = models.IntegerField(choices=DAYS_OF_WEEK)
    end_day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
