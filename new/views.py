from django.shortcuts import render,redirect
from django.core.handlers.wsgi import WSGIRequest
from .models import Course,Lesson
from .forms import CourseForm,LessonForm

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

def add_course(request: WSGIRequest):
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.create()
            return redirect('main', pk=post.pk)
    else:
        form = CourseForm()
    context = {
        "form": form
    }
    return render(request, 'add_post.html', context)

def add_lesson(request:WSGIRequest):
    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.create()
            return redirect('detail', pk=post.pk)
    else:
        form = CourseForm()
    context = {
        "form": form
    }
    return render(request, 'add_lesson.html', context)
