from django.shortcuts import render
from django.views.generic.edit import DeleteView
from myapp.models import Student

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/success/'
    template_name = 'myapp/studel.html'