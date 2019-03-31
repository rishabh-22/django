from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    books = models.CharField(max_length=70)
    number_of_books = models.IntegerField(max_length=4)
