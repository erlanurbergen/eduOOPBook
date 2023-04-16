from django.contrib import admin
from django.urls import path, include

from oopBook import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('/classes', views.classes, name = 'classes'),
    path('/encapsulation', views.encapsulation, name = 'encapsulation'),
    path('/inheritance', views.inheritance, name = 'inheritance'),
    path('/class_attributes', views.class_attributes, name = 'class_attributes'),
    path('/overridding', views.overridding, name = 'overridding'),
    path('/object', views.object, name = 'object'),
    path('/video_lessons', views.video_lessons, name = 'video_lessons'),
    path('/additional_info', views.additional_info, name = 'additional_info'),
    path('/tests', views.tests, name = 'tests'),
    path('/tasks', views.tasks, name = 'tasks'),
]