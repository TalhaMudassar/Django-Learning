from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from myapp.models import Student


class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','roll']
    success_url = '/student/'
    template_name = 'myapp/student_form.html'
    
class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'myapp/student_list.html'
    
    
class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'myapp/student_detail.html'
    
    
    
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','email','roll']
    success_url = '/student/'
    template_name = 'myapp/student_form.html'
    
class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student/'
    template_name = 'myapp/student_confirm_delete.html'
    
    
