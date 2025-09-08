from django.shortcuts import render
from student.forms import Registration,Adress,login
# Create your views here.

def registration(req):
    fm = Registration(auto_id=True,initial={'email':'xyz@example.com'})
    return render(req,'student/registration.html',{'form':fm})

def Adresses(req):
    fm = Adress(auto_id=True)
    return render(req,'student/adress.html',{'form':fm})

def Login(req):
    fm = login()
    return render(req,'student/login.html',{'form':fm}) 
