from django import forms

from .models import Course,Lesson


class CourseForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "placeholder": "Curs nomi",
        'class': "form-control"
    }))
    info = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Curs haqida malumot kiriting",
        'class': "form-control",
        "rows": 3
    }))
    cours_logo = forms.ImageField(required=False, widget=forms.FileInput())

    def create(self):
        course = Course.objects.create(**self.cleaned_data)
        return course
class LessonForm(forms.Form):
    lesson_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "Lesson nomi",
        'class': "form-control"
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Lesson haqida malumot kiriting",
        'class': "form-control",
        "rows": 2
    }))
    will_be = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "placeholder":"Qachon boladi"
    }))
    photo = forms.ImageField(required=False, widget=forms.FileInput())

    course =forms.ModelChoiceField(queryset=Course.objects.all(),
                                      widget=forms.Select(attrs={
                                          "class": "form-select"
                                      }))

    def create(self):
        lesson = Lesson.objects.create(**self.cleaned_data)
        return lesson
