from django.shortcuts import render
from school.models import Student
from datetime import date,time

    # Create your views here.
def home(request):
    # student_data = Student.objects.all() 
    # student_data = Student.objects.filter(name__exact='sonam') 
    # student_data = Student.objects.filter(name__iexact='sonam') 
    # student_data = Student.objects.filter(name__contains='r')
    # student_data = Student.objects.filter(name__icontains='s') 
    # student_data = Student.objects.filter(id__in=[1,3,7]) 
    # student_data = Student.objects.filter(marks__gte=200) 
    # student_data = Student.objects.filter(marks__lt=200) 
    # student_data = Student.objects.filter(marks__lte=200) 
    # student_data = Student.objects.filter(name__startswith='S') with case senstive 
    # student_data = Student.objects.filter(name__istartswith='S') with out case senstive
    # student_data = Student.objects.filter(name__endswith='S')
    # student_data = Student.objects.filter(name__iendswith='t')  
    # student_data = Student.objects.filter(pass_date__range=('2024-1-1','2025-9-10')) 
    # student_data = Student.objects.filter(admission_date__date=date(2025,9,2)) 
    # student_data = Student.objects.filter(admission_date__date__gt=date(2025,9,2))
    # student_data = Student.objects.filter(admission_date__date__lt=date(2025,9,2))
    # student_data = Student.objects.filter(pass_date__year=2024)
    # student_data = Student.objects.filter(pass_date__month=1)
    # student_data = Student.objects.filter(pass_date__month_gt=5)
    # student_data = Student.objects.filter(pass_date__day__gt=5)
    # student_data = Student.objects.filter(pass_date__week=15)
    # student_data = Student.objects.filter(pass_date__week__gt=15)
    # student_data = Student.objects.filter(pass_date__week__lt=5)
    # student_data = Student.objects.filter(pass_date__week_day=5)
    # student_data = Student.objects.filter(pass_date__week_day__gt=5)
    # student_data = Student.objects.filter(pass_date__quarter=1)
    # student_data = Student.objects.filter(pass_date__quarter__gt=1)
    # student_data = Student.objects.filter(admission_date__time=time(12,46))
    # student_data = Student.objects.filter(admission_date__time__gt=time(6,25))
    # student_data = Student.objects.filter(admission_date__time=time(6,25))
    # student_data = Student.objects.filter(admission_date__hour__gt=5)
    # student_data = Student.objects.filter(admission_date__minute=40)
    # student_data = Student.objects.filter(admission_date__minute__gt=40)
    # student_data = Student.objects.filter(admission_date__second=40)
    # student_data = Student.objects.filter(admission_date__second__gt=40)
    
    student_data = Student.objects.filter(roll__isnull=False)
    
    
        
        
    print("Students Data:",student_data)
    return render(request,'school/home.html',{'students':student_data})
