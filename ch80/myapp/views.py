from django.shortcuts import render
from django.views import View
from myapp.models import Student
from django.views.generic.list import ListView

class AllStudentView(View):
    def get(self,request):
        all_students = Student.objects.all()
        return render(request,'myapp/all_student.html',{'all_students':all_students})
    
class StudentListView(ListView):
    model = Student
    
    
class StudentListView1(ListView):
    model = Student
    template_name_suffix = '_all'
    ordering = ['name'] # we ordering on the base of name
    
    
class StudentListView2(ListView):
    model = Student
    template_name = 'myapp/students.html'  # template.html completely name change
    context_object_name = 'students'  # from this we change the the context name
    
    
class StudentListView3(ListView):
    model = Student
    template_name = 'myapp/sabhistudents.html'  
    context_object_name = 'students'  
    
    # if we write these we get all the objects  same as all method 
    def get_queryset(self): 
        return Student.objects.filter(course = 'python')
    #another context name 
    def get_context_data(self, *args,**kwargs) :
        context = super().get_context_data(*args,**kwargs)
        context["django_students"] = Student.objects.filter(course = 'django')
        return context
    
    #in this we check if the cookie are sonam 
    def get_template_names(self):
        if self.request.COOKIES.get('user') == 'sonam':
            template_name = 'myapp/sonam.html'
        else:
            template_name = self.template_name
        return [template_name]
    
    

