from django.contrib import admin
from student.models import User
# Register your models here.

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['id','name','email','passward']