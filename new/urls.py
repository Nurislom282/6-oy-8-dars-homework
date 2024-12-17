from django.urls import path
from .views import home,lesson_by_course,lessondetail,add_course,add_lesson

urlpatterns = [
    path('',home,name='main'),
    path('course/<int:course_id>/', lesson_by_course, name='lesson_by_course'),
    path('lesson/<int:pk>/',lessondetail,name='detail'),
    path('add-post/', add_course, name='add_course'),
    path('add-lesson/', add_lesson, name='add_lesson'),
]