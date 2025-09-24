from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Student
from django import forms
from myapp.forms import StudentForm


# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name','email','password']
#     success_url = '/thanks/'


#if we want custom template 
# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name','email','password']
#     success_url = '/thanks/'
#     template_name = 'myapp/register.html'



# #custmize form field
# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name','email','password']
#     success_url = '/thanks/'
#     template_name = 'myapp/register.html'
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'myform'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
#         return form


#if we use model form :
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = '/thanks/'
    template_name = 'myapp/register.html'

    