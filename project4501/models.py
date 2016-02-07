from django.db import models
from django.db.models import Count, Min, Sum, Avg, Max
from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone


class User(models.Model):
	user_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length=20)
	phone = models.IntegerField()
	description = models.TextField()
	grade = models.IntegerField(default = 0)
	courses = models.ManyToManyField(Course, blank = True, related_name = 'users')


class Course(models.Model):
	class_id = models.IntegerField(primary_key = True)
	qualification = models.CharField(max_length=30)

class Review(models.Model):
	review_id = models.IntegerField(primary_key = True)
	writer = models.ForeignKey('User', related_name = 'writters')
    receiver = models.ForeignKey('User', related_name = 'receivers')
    course = models.ForeignKey('Course')

