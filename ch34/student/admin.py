from django.contrib import admin
from student.models import Profilee
# Register your models here.
@admin.register(Profilee)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','address','passward')