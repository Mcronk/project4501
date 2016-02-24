from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from project4501.serializers import UserSerializer, CourseSerializer, ReviewSerializer, SessionSerializer, MessageSerializer, ApplicationSerializer
from project4501.models import User, Course, Review, Session, Message, Application
# from project4501.serializers import UserSerializer, CourseSerializer, ReviewSerializer, AdditionInfoSerializer, SessionSerializer, MessageSerializer, ApplicationSerializer
# from project4501.models import User, Course, Review, AdditionInfo, Session, Message, Application

from django.http import Http404
from rest_framework.views import APIView

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import routers, serializers, viewsets, generics
#hi

#USER: listing all the existing users, or creating a new user.
@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#USER: used to retrieve, update or delete the individual user.
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve, update or delete a user instance.
    """
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#COURSE: listing all the existing courses, or creating a new course.
class course_list(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#COURSE: used to retrieve, update or delete the individual course.
class course_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer





class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

# class AdditionInfoViewSet(viewsets.ModelViewSet):
#     queryset = AdditionInfo.objects.all()
#     serializer_class = AdditionInfoSerializer

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

def base(request):
    return render(request, 'base.html')

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

#OLD_USER: listing all the existing users, or creating a new user.
# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many = True, context={'request': request})
#         return JSONResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser.parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400) 
#     #elif request.method == 'DELETE':
#     #    user.delete()
#     #    return HttpResponse(status=204)

#OLD_USER: used to retrieve, update or delete the individual user.
# @csrf_exempt
# def user_detail(request, uid):
#     try:
#         user = User.objects.get(user_id=uid)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JSONResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)


#OLD_COURSE: listing all the existing courses, or creating a new course.
# def course_list(request):
#     #course = Course.get(pk=pk)
#     if request.method == 'GET':
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many = True)
#         return JSONResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser.parse(request)
#         serializer = CourseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#     #elif request.method == 'DELETE':
#     #    course.delete()
#     #    return HttpResponse(status=204)    

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


