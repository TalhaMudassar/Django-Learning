from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
class Post(models.Model):
  title = models.CharField(max_length=255)
  content = CKEditor5Field(config_name='extends')
