from django.shortcuts import render
from school.models import Student
# Create your views here.
def home(request):
    student_data = Student.objects.get(pk=3)
    # student_data = Student.objects.first()
    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').first
    # student_data = Student.objects.earliest('pass_date')
    
    
    # student_data = Student.objects.all()
    # print(student_data.exists())
    
    # one_data = Student.objects.get(pk=2)
    # print(student_data.filter(pk=one_data.pk).exists())
    
    
    # student_data = Student.objects.create(name='zarawar',roll=114,city='karachi',marks=70,pass_date='2025-5-4')
    # print(f"student_data {student_data}")
    
    # student_data,created = Student.objects.get_or_create(name='zarawar',roll=114,city='karachi',marks=70,pass_date='2025-5-4')
    # print(created)
    
    # student_data = Student.objects.filter(id=1).update(name='kabir')
    
    # student_data = Student.objects.filter(marks=100).update(city='islamabad')
    
    # student_data , created = Student.objects.update_or_create(id=10,name='kinza',defaults={'name':"samina",'roll':157,'marks':200,'pass_date':'2025-5-4'})
    
    # objs = [
    # Student(name='Atif', roll=116, city='Dhanbad', marks=70, pass_date='2020-5-4'),
    # Student(name='Sahil', roll=117, city='Bokaro', marks=50, pass_date='2020-5-6'),
    # Student(name='Kumar', roll=118, city='Dhanbad', marks=30, pass_date='2020-5-9'),
    # ]
    # student_data = Student.objects.bulk_create(objs)

    
    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city="rawilpindi"
    # student_data = Student.objects.bulk_update(all_student_data,['city'])
     
    
    # student_data = Student.objects.in_bulk([1, 3])
    # print(student_data[3].name)
    
    # student_data = Student.objects.get(pk=1).delete()
    
    # student_data = Student.objects.filter(marks=30).delete()
    
    
    # tudent_data = Student.objects.all().delete()
    print(Student.objects.all().count()) 

    print(f"student_data {student_data}")
        
    return render(request,'school/home.html',{'student':student_data})


