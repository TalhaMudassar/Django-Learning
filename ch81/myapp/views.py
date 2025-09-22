from django.shortcuts import render
from myapp.models import Student
from django.views import View
from django.views.generic.detail import DetailView


class SingleStudentView(View):
    def get(self,request,pk):
        single_student_data = Student.objects.get(pk=pk)
        return render(request,'myapp/single_student_data.html',{'single_student':single_student_data})
    

class StudentDetailView(DetailView):
    model = Student
    
    
class StudentDetailView1(DetailView):
    model = Student
    pk_url_kwarg = 'geek'  # use this for url name change like <int:pk> use geek in this case instead of pk
    
    
    
class StudentDetailView2(DetailView):
    model = Student
    pk_url_kwarg = 'geek'
    template_name_suffix = '_jankari' # use this for template name change 
    
    
class StudentDetailView3(DetailView):
    model = Student
    pk_url_kwarg = 'geek'
    template_name = 'myapp/student.html' # if we want to change the complet name  of the tempalte 
    
    
class StudentDetailView4(DetailView):
    model = Student
    template_name = 'myapp/newstudent.html'
    context_object_name = 'stu'
    
    
    
class StudentDetailView5(DetailView):
    model = Student
    template_name = 'myapp/students1.html'
    context_object_name = 'student'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] =  Student.objects.all().order_by('name')
        return context
    
    



