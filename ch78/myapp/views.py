from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class AboutTemplateView(TemplateView):
    template_name ='myapp/about.html'
    
class ContactTemplateView(TemplateView):
    template_name = 'myapp/contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'Sonam'
        context["roll"] = 101  
        return context
    

class ProfileTemplateView(TemplateView):
    template_name = 'myapp/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "TALHA" 
        print(context)
        return context
    
     