from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django import forms
from myapp.forms import StudentForm

# class StudentCreateView(CreateView): # it demands the template with specific name student form
#     model = Student
#     fields = ['name','email','password']
#     success_url = '/thanks/'   # we set the successurl if data submitted 


# class StudentCreateView(CreateView): # it demands the template with specific name student form
#     model = Student
#     fields = ['name','email','password']



# class StudentCreateView(CreateView): # it demands the template with specific name student form
#     model = Student
#     fields = ['name','email','password']
#     template_name = 'myapp/register.html'
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
#         form.fields['password'].widget = forms.TextInput(attrs={'class':'mypass'})
#         return form




class StudentCreateView(CreateView): # it demands the template with specific name student form
    form_class = StudentForm
    model = Student
    template_name = 'myapp/register.html'  # now we must use that because we use form our createview can not give me our default tempalte 
 
   
    
