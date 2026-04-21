# models.py
from django.db import models


class FriendPhoto(models.Model):
    title = models.CharField(max_length=100, verbose_name="Rasm nomi")
    image = models.ImageField(upload_to='photos/ustoz', verbose_name="Rasm")
    description = models.TextField(verbose_name="Izoh", help_text="Uzunroq izoh yozing")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StudentPhoto(models.Model):
    title = models.CharField(max_length=100, verbose_name="Rasm nomi")
    image = models.ImageField(upload_to='photos/uquv', verbose_name="Rasm")
    description = models.TextField(verbose_name="Izoh", help_text="Uzunroq izoh yozing")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)  # Email unikal bo'lishi kerak
    dob = models.DateField()

    def __str__(self):
        return self.email

class Taklif(models.Model):
    fikr = models.TextField()  # Fikr matnini saqlash uchun
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana va vaqt

    def __str__(self):
        return self.fikr[:50]  # Fikrning birinchi 50 ta belgisini ko'rsatish
    
    
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 