from django.db import models
from django.db.models import Count, Min, Sum, Avg, Max
from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone

class Course(models.Model):
	class_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=20)
	description = models.TextField()

class User(models.Model):
	user_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	email = models.CharField(max_length = 20)
	phone = models.IntegerField()
	description = models.TextField()
	grade = models.IntegerField(default = 0)

	courses = models.ManyToManyField(Course, blank = True, related_name = 'users')

class Review(models.Model):
	review_id = models.IntegerField(primary_key = True)
	content = models.TextField()

	writer = models.ForeignKey('User', related_name = 'writter')
	receiver = models.ForeignKey('User', related_name = 'receiver')
	course = models.ForeignKey('Course')

class Strength(models.Model):
	strength_id = models.IntegerField(primary_key = True)
	qualification = models.CharField(max_length=30)

	course = models.ForeignKey('Course')
	tutor = models.ForeignKey('User')

class Session(models.Model):
	session_id = models.IntegerField(primary_key = True)
	time = models.DateTimeField('Class Time')
	price = models.IntegerField()

	tutor = models.ForeignKey('User', related_name = 'tutor')
	student = models.ForeignKey('User', related_name = 'student')
	course = models.ForeignKey('Course')



