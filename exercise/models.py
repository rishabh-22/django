from django.db import models

# Create your models here.


class Manager(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    Department = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now=True, null=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    salary = models.IntegerField(max_length=9)
    Designation = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now=True, null=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True)
    reporting_manager = models.ForeignKey(Manager, null=True, on_delete=models.CASCADE)
