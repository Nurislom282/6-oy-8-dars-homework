from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150,unique=True,verbose_name="Kurs nomi")
    info = models.TextField(verbose_name="Kurs haqida malumot")
    create_at = models.DateTimeField(auto_now_add=True,verbose_name="qoshilgan Vaqti")
    update_at = models.TimeField(auto_now=True,verbose_name="Yangilangal vaqti")
    cours_logo = models.ImageField(upload_to='curslogos/',verbose_name="curs logosi")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100,unique=True,verbose_name='Dars nomi')
    description = models.TextField(verbose_name='dars haqida')
    will_be = models.DateTimeField(verbose_name="Qchon boladi")
    photo = models.ImageField(upload_to='lessonphotos/',verbose_name="dars rasmi")
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name