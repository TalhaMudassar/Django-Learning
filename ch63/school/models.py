from django.db import models
from school.managers import CustomStudentManager

class Student(models.Model):
 name = models.CharField(max_length=70)
 roll = models.IntegerField(unique=True, null=False)
 city = models.CharField(max_length=70)
 marks = models.IntegerField()
 pass_date = models.DateField()
 admission_date=models.DateTimeField()
 
 
 #manager name changing 
#  objects = models.Manager()
#  students = models.Manager() # this can create automatically if we dont create it 


# custommanager
#  objects = CustomStudentManager()
 students = CustomStudentManager()


# class ProxyStudent(Student):
#  students = CustomStudentManager()
#  class Meta:
#   proxy = True
#   ordering = ['name']
