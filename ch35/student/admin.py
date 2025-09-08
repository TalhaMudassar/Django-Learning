from django.contrib import admin
from student.models import Profile
# Register your models here.

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display= ('id','name','email','passward')
