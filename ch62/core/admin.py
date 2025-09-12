from django.contrib import admin
from core.models import Student,Teacher,Contractor,Exam_center,Candiate,Product,DiscountProduct
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','fees']
    
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','salary','join_date']
    
    
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','payment','join_date']
    
    
@admin.register(Exam_center)
class Exam_center_Admin(admin.ModelAdmin):
    list_display= ['id','center_name','center_city']
    
@admin.register(Candiate)
class Candiate_Admin(admin.ModelAdmin):
    list_display= ['id','center_name','center_city','name','roll']
    
    
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'price', 'stock']

@admin.register(DiscountProduct)
class DiscountedProductAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'price', 'stock']
    
    
