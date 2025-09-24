from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField()
    roll = models.IntegerField()
    course = models.CharField()
