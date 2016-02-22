from django.db import models
from django.db.models import Count, Min, Sum, Avg, Max
from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime  

class User(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	email = models.CharField(max_length = 20)
	phone = models.IntegerField(blank = True, null = True)
	description = models.TextField(blank = True)
	grade = models.IntegerField(default = 0)
	# courses = models.ManyToManyField(Course, blank = True, related_name = 'users')

class Course(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=20)
	tag = models.CharField(max_length=20, blank = True)
	description = models.TextField(null = True)
	popularity = models.IntegerField(default = 0)
	qualification = models.CharField(max_length=30, blank = True)
	available_time = models.DateTimeField(default=datetime.now, blank=True)
	#should be a list of available time
	price = models.IntegerField(default = -1)

	tutor = models.ForeignKey('User', related_name = 'tutoring_courses', null=True)
	# student = models.ForeignKey('User', related_name = 'taking_courses', null=True)

class Session(models.Model):
	id = models.IntegerField(primary_key = True)
	time = models.DateTimeField('Class Time')
	
	# tutor = models.ForeignKey('User', related_name = 'tutor')
	student = models.ManyToManyField('User', related_name = 'student_session')
	course = models.ForeignKey('Course', related_name = 'course_session')

class Review(models.Model):
	id = models.IntegerField(primary_key = True)
	content = models.TextField()

	writer = models.ForeignKey('User', related_name = 'writter_review')
	# receiver = models.ForeignKey('User', related_name = 'receiver')
	course = models.ForeignKey('Course', related_name = 'course_review')

# class AdditionInfo(models.Model):
# 	info_id = models.IntegerField(primary_key = True)
# 	qualification = models.CharField(max_length=30)
# 	available_time = models.DateTimeField('Available Time')
# 	price = models.IntegerField(default = -1)
# 	course = models.ForeignKey('Course')
# 	tutor = models.ForeignKey('User')


class Message(models.Model):
	id = models.IntegerField(primary_key = True)
	content = models.TextField()

	sender = models.ForeignKey('User', related_name = 'sender_message')
	receiver = models.ForeignKey('User', related_name = 'receiver_message')

class Application(models.Model):
	id = models.IntegerField(primary_key = True)
	price = models.IntegerField(default = -1)
	content = models.TextField(blank = True)
	# tutor = models.ForeignKey('User', related_name = 'applicationtutor')
	student = models.ForeignKey('User', related_name = 'student_application')
	course = models.ForeignKey('Course', related_name = 'course_application')

