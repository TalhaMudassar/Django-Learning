from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=50)
    roll = models.IntegerField()
    

    
class Result(models.Model):
    stu_class = models.CharField(max_length=70)
    marks = models.IntegerField()
    

    
    
