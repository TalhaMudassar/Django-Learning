from django.db import models

# Create your models here.
class Profilee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    passward = models.CharField(max_length=255)