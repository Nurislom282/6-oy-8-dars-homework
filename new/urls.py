from django.urls import path
from .views import home,lesson_by_course,lessondetail

urlpatterns = [
    path('',home,name='main'),
    path('course/<int:course_id>/', lesson_by_course, name='lesson_by_course'),
    path('lesson/<int:pk>/',lessondetail,name='detail'),
]