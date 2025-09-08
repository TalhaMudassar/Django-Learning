from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)
    roll = models.IntegerField()
    state = models.CharField(max_length=70)
    comment = models.TextField(max_length=255,default='Here are simple comments')
    
#command for running or making database ....
# python manage.py makemigratation
# python manage.py makemigrate  

#show migrations
#sql mig  