"""project4501 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views
from project4501.views import UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile),
    url(r'^search/', views.search),
    url(r'^signup/', views.signup),
    url(r'^appointment/', views.appointment),
    url(r'^user/', include(router.urls)),
    url(r'^users/$',views.user_list),
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail),

    url(r'^courses/$',views.course_list.as_view()),
    url(r'^courses/(?P<pk>[0-9]+)/$', views.course_detail.as_view()),

    url(r'^review_list/',views.review_list),
    url(r'^additioninfo_list/', views.additioninfo_list),
    url(r'^session_list/', views.session_list),
    url(r'^message_list/', views.message_list),
    url(r'^application_list/', views.application_list),
    #(?P<pk>[0-9]+)/$
]







