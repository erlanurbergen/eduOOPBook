from django.shortcuts import render
from .models import Topics
# Create your views here.

def index(request) :
    return render(request, 'oopBook/index.html')


def classes(request) :
    context = {
        "classes" : Topics.objects.all()
    }
    return render(request, 'oopBook/classes.html', context)


def encapsulation(request) :
    context = {
        "encap": Topics.objects.filter(name='Инкапсуляция')
    }
    return render(request, 'oopBook/encapsulation.html', context)


def inheritance(request) :
    context = {
        "inher" : Topics.objects.filter(name='Наследование')
    }
    return render(request, 'oopBook/inheritance.html', context)


def class_attributes(request) :
    context = {
        "attributes" : Topics.objects.filter(name = 'Аттрибуты классов')
    }
    return render(request, 'oopBook/class_attributes.html', context)


def additional_info(request) :
    context = {
        'additional' : Topics.objects.filter(name = 'Дополнительные источники')
    }
    return render(request, 'oopBook/additional_info.html', context)


def object(request) :
    context = {
        'object': Topics.objects.filter(name = 'класс Object')
    }
    return render(request, 'oopBook/object.html', context)

def video_lessons(request) :
    context = {
        "video_lessons": Topics.objects.filter(name = 'Видеоуроки')
    }
    return render(request, 'oopBook/video_lessons.html', context)

def overridding(request) :
    context = {
        "override": Topics.objects.filter(name='Переопределение классов')
    }
    return render(request, 'oopBook/overridding.html', context)


def tests(request) :
    return render(request, 'oopBook/tests.html')

def tasks(request) :
    return render(request, 'oopBook/tasks.html')


