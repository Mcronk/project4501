from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import routers, serializers, viewsets
from project4501.models import User, Course, Review, AdditionInfo, Session, Message, Application

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'name', 'password', 'email', 'phone', 'description', 'grade', 'courses')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_date.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.description = validated_data.get('description', instance.description)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('class_id', 'name', 'tag', 'description', 'popularity')

    def create(self, validated_data):
        return COurse.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.description = validated_data.get('description', instance.description)
        instance.popularity = validated_data.get('popularity', instance.popularity)

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

class AdditionInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdditionInfo
        fields = ('qualification', 'available_time', 'price', 'course', 'tutor')

    def create(self, validated_data):
        return AdditionInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.qualification = validated_data.get('qualification', instance.qualification)
        instance.available_time = validated_data.get('available_time', instance.available_time)
        instance.price = validated_data.get('price', instance.price)
        instance.course = validated_data.get('course', instance.course)
        instance.tutor = validated_data.get('tutor', instance.tutor)

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

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class AdditionInfoViewSet(viewsets.ModelViewSet):
    queryset = AdditionInfo.objects.all()
    serializer_class = AdditionInfoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    return render(request, 'signup.html')

def appointment(request):
    return render(request, 'appointment.html')

def user_list(request):
    #user = User.get(pk=pk)
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400) 
    #elif request.method == 'DELETE':
    #    user.delete()
    #    return HttpResponse(status=204)

def course_list(request):
    #course = Course.get(pk=pk)
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    #elif request.method == 'DELETE':
    #    course.delete()
    #    return HttpResponse(status=204)    

def review_list(request):
    #review = Review.get(pk=pk)
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    #elif request.method == 'DELETE':
    #    review.delete()
    #    return HttpResponse(status=204)

def additioninfo_list(request):
    #info = AdditionInfo.get(pk=pk)
    if request.method == 'GET':
        infos = AdditionInfo.objects.all()
        serializer = AdditionInfoSerializer(infos, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = AdditionInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    #elif request.method == 'DELETE':
    #    info.delete()
    #    return HttpResponse(status=204)

def session_list(request):
    #session = Session.get(pk=pk)
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = SessionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    #elif request.method == 'DELETE':
    #    info.delete()
    #    return HttpResponse(status=204)

def message_list(request):
    #messages = Message.get(pk=pk)
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    #elif request.method == 'DELETE':
    #    message.delete()
    #    return HttpResponse(status=204)

def application_list(request):
    #applications = Application.get(pk=pk)
    if request.method == 'GET':
        messages = Application.objects.all()
        serializer = ApplicationSerializer(messages, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = ApplicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    #elif request.method == 'DELETE':
    #    applications.delete()
    #    return HttpResponse(status=204)


