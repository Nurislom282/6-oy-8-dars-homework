from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Course,Lesson


def home(request:WSGIRequest):
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    context = {
        'courses': courses,
        'lessons': lessons
    }
    return render(request,'index.html',context)

def lesson_by_course(request:WSGIRequest,course_id):
    courses = Course.objects.all()
    lessons = Lesson.objects.filter(course_id=course_id)
    context = {
        'courses': courses,
        'lessons': lessons
    }
    return render(request,'index.html',context)

def lessondetail(request:WSGIRequest,pk):
    lesson = Lesson.objects.get(pk=pk)
    courses = Course.objects.all()
    context = {
        'lesson': lesson,
        'courses':courses
    }
    return render(request,'detail.html',context)
