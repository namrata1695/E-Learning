from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

class Course(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)

class Student(User):
    LVL_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('ND', 'No Degree'),
    ]

    level = models.CharField(choices=LVL_CHOICES, max_length=2, default='HS')
    address = models.CharField(max_length=300)
    province=models.CharField(max_length=2)
    registered_courses = models.ManyToManyField(Course, blank=True)
    interested_in = models.ManyToManyField(Topic)


