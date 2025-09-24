from django.shortcuts import render,HttpResponse
from django.views.generic.edit  import FormView
from myapp.forms import ContactForm,Student_Contact_Form
from django.contrib import messages
from myapp.models import Students


# class ContactFormView(FormView):
#     template_name = 'myapp/contact.html'
#     form_class = ContactForm
    # def form_valid(self, form): # her is the function for checking validity of the form 
    #     print(form)  # here the completely form data get's in it we can use accourding to our needs
    #     print(form.cleaned_data['name'])
    #     print(form.cleaned_data['email'])
    #     print(form.cleaned_data['msg'])
        
    #     return super().form_valid(form)
    #     # return HttpResponse("Thnaks for submission ") #we can also use this for submitting
    
   
   
class ContactFormView(FormView):
    template_name = 'myapp/contact.html'
    form_class = ContactForm
    success_url = '/thank_you/'
    initial = {'name':'soman'}
    
    def form_valid(self, form):
        print(form)
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        messages.error
        (self.request,'invalid form field')
        response = super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra"] = True 
        return context
    
    
class StudentFormView(FormView):
    template_name = 'myapp/register.html'
    form_class = Student_Contact_Form

    def form_valid(self, form):
        name = form.cleaned_data['name']
        roll = form.cleaned_data['roll']
        course = form.cleaned_data['course']
        student = Students(
            name = name,
            roll = roll,
            course = course,
        )
        student.save()
        return HttpResponse("Your form submitted")
    
    
    def form_invalid(self, form):
        messages.error
        (self.request,'invalid form field')
        response = super().form_invalid(form)
        

    
       
    
    
        
    
 