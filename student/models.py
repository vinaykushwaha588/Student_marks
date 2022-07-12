
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    mobile = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(unique=True,blank=True,null=True)
    address = models.TextField(max_length=200,blank=True,null=True)
    admission_date = models.DateField(auto_now=True,blank=True,null=True)
    updated_date = models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name

class Mark(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    physics = models.BigIntegerField(blank=True,null=True)
    chemistry = models.BigIntegerField(blank=True,null=True)
    math = models.BigIntegerField(blank=True,null=True)

 