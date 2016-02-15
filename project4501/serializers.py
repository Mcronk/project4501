from rest_framework import serializers

from project4501.models import User, Course, Review, Session, Message, Application

# from project4501.models import User, Course, Review, AdditionInfo, Session, Message, Application
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'name', 'tag', 'description', 'popularity', 'qualification', 'available_time', 'price')

class UserSerializer(serializers.ModelSerializer):
	tutoring_courses = CourseSerializer(many=True)
	taking_courses = CourseSerializer(many=True)
	
	class Meta:
		model = User
		#ommiting courses temporarily
		fields = ('id', 'name', 'password', 'email', 'phone', 'description', 'grade', 'tutoring_courses', 'taking_courses')
	
	def create(self, validated_data):
		tutoring_courses_data = validated_data.pop('tutoring_courses')
		taking_courses_data = validated_data.pop('taking_courses')

		user = User.objects.create(**validated_data)

		# for tutoring_course_data in tutoring_courses_data:
		# 	Course.objects.create(tutor=user, **tutoring_course_data)
		# for taking_course_data in taking_courses_data:
		# 	course = Course.objects.get(id = taking_course_data[id])
		# 	course.student = user
		# 	course.save()
		return user


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('user_id', 'name', 'password', 'email', 'phone', 'description', 'grade')

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.password = validated_date.get('password', instance.password)
#         instance.email = validated_data.get('email', instance.email)
#         instance.phone = validated_data.get('phone', instance.phone)
#         instance.description = validated_data.get('description', instance.description)
#         instance.grade = validated_data.get('grade', instance.grade)
#         instance.save()
#         return instance

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Course
#         fields = ('class_id', 'name', 'tag', 'description', 'popularity')

#     def create(self, validated_data):
#         return COurse.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.tag = validated_data.get('tag', instance.tag)
#         instance.description = validated_data.get('description', instance.description)
#         instance.popularity = validated_data.get('popularity', instance.popularity)

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Review
		fields = ('review_id', 'content', 'writer', 'receiver', 'course')

	def create(self, validated_data):
		return Review.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.content = validated_data.get('content', instance.content)
		instance.writer = validated_data.get('writer', instance.writer)
		instance.receiver = validated_data.get('receiver', instance.receiver)
		instance.course = validated_data.get('course', instance.course)

# class AdditionInfoSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = AdditionInfo
# 		fields = ('qualification', 'available_time', 'price', 'course', 'tutor')

# 	def create(self, validated_data):
# 		return AdditionInfo.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.qualification = validated_data.get('qualification', instance.qualification)
# 		instance.available_time = validated_data.get('available_time', instance.available_time)
# 		instance.price = validated_data.get('price', instance.price)
# 		instance.course = validated_data.get('course', instance.course)
# 		instance.tutor = validated_data.get('tutor', instance.tutor)

class SessionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Session
		fields = ('time', 'tutor', 'student', 'course')

	def create(self, validated_data):
		return Session.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.time = validated_data.get('time', instance.time)
		instance.tutor = validated_data.get('tutor', instance.tutor)
		instance.student = validated_data.get('price', instance.student)
		instance.course = validated_data.get('course', instance.course)

class MessageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Message
		fields = ('content', 'sender', 'receiver')

	def create(self, validated_data):
		return Message.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.content = validated_data.get('content', instance.content)
		instance.sender = validated_data.get('sender', instance.sender)
		instance.receiver = validated_data.get('receiver', instance.receiver)

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Application
		fields = ('price', 'content', 'tutor', 'student', 'course')

	def create(self, validated_data):
		return Application.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.price = validated_data.get('price', instance.price)
		instance.content = validated_data.get('content', instance.content)
		instance.tutor = validated_data.get('tutor', instance.tutor)
		instance.student = validated_data.get('student', instance.student)
		instance.course = validated_data.get('course', instance.course)
