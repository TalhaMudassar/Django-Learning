from django.shortcuts import render
from student.forms import DemoForm
# Create your views here.

def demofiles(req):
    fm = DemoForm
    return render(req,'student/demoform.html',{'form':fm})
