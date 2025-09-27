from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import FormView 
from account.forms import RegistrationForm
from account.models import User

class HomeView(View):
    def get(self,request, *args,**kwargs):
        return render(request,'account/home.html')
    
class LoginView(View):
    def get(self,request, *args,**kwargs):
        return render(request,'account/login.html')
    
    def post(self,request, *args,**kwargs):
        return render(request,'customer/dashboard.html')
    
    
class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'account/register.html'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = False # Account inactive until email is verified 
        user.save()
        return redirect('login')
      
    

    
    
class CustomPasswordResetView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'account/password_reset.html')
    
    
class PasswordResetConfirmView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'account/password_reset_confirm.html')
    
    
    
    
