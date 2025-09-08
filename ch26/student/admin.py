from django.contrib import admin
from student.models import Result,profile
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    list_display = ('name','email')
     
admin.site.register(profile,profileAdmin)


#using decorator:
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','stu_class')

