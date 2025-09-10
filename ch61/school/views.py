from django.shortcuts import render
from school.models import Student
from django.db.models import Q
def home(request):
 
 student_data = Student.objects.all()[:5]
#  student_data = Student.objects.all()[5:10]
#  student_data = Student.objects.all()[:10:2]
#  student_data = Student.objects.all()[3:10:3]

 context = {'students':student_data}
 
 return render(request, 'school/home.html', context)