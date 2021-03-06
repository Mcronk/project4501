from django.db import models
from django.db.models import Count, Min, Sum, Avg, Max
from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone

class Course(models.Model):
	class_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=20)
	tag = models.CharField(max_length=20, blank = True)
	description = models.TextField(null = True)
	popularity = models.IntegerField(default = 0)

class User(models.Model):
	user_id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	email = models.CharField(max_length = 20)
	phone = models.IntegerField(blank = True, null = True)
	description = models.TextField(blank = True)
	grade = models.IntegerField(default = 0)

	courses = models.ManyToManyField(Course, blank = True, related_name = 'users')

class Review(models.Model):
	review_id = models.IntegerField(primary_key = True)
	content = models.TextField()

	writer = models.ForeignKey('User', related_name = 'writter')
	receiver = models.ForeignKey('User', related_name = 'receiver')
	course = models.ForeignKey('Course')

class AdditionInfo(models.Model):
	info_id = models.IntegerField(primary_key = True)
	qualification = models.CharField(max_length=30)
	available_time = models.DateTimeField('Available Time')
	price = models.IntegerField(default = -1)
	course = models.ForeignKey('Course')
	tutor = models.ForeignKey('User')

class Session(models.Model):
	session_id = models.IntegerField(primary_key = True)
	time = models.DateTimeField('Class Time')
	
	tutor = models.ForeignKey('User', related_name = 'tutor')
	student = models.ForeignKey('User', related_name = 'student')
	course = models.ForeignKey('Course')

class Message(models.Model):
	message_id = models.IntegerField(primary_key = True)
	content = models.TextField()
	sender = models.ForeignKey('User', related_name = 'msender')
	receiver = models.ForeignKey('User', related_name = 'mreceiver')

class Application(models.Model):
	application_id = models.IntegerField(primary_key = True)
	price = models.IntegerField(default = -1)
	content = models.TextField(blank = True)
	tutor = models.ForeignKey('User', related_name = 'applicationtutor')
	student = models.ForeignKey('User', related_name = 'applicationstudent')
	course = models.ForeignKey('Course')