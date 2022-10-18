from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=25)
    number = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    doctor = models.CharField(max_length=25)
    date = models.CharField(max_length=25)
