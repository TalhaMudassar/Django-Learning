from django.db import models

# Abstract table inheritance
class BaseModel(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    join_date = models.DateField()
    
    class Meta:
        abstract = True
        
        
class Student(BaseModel):
    fees = models.IntegerField()
    join_date = None
    
class Teacher(BaseModel):
    salary = models.IntegerField()
    
    
class Contractor(BaseModel):
    payment = models.IntegerField()
    join_date = models.DateTimeField()
    
    
#Multi table inheritance 
class Exam_center(models.Model):
    center_name = models.CharField(max_length=255)
    center_city = models.CharField(max_length=255)
    
class Candiate(Exam_center):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    
    
    
    
#PROXY MODEL
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    

class DiscountProduct(Product):
    class Meta:
        proxy = True
        ordering= ['id']
    