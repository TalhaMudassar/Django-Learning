from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            passward = form.cleaned_data['passward']
            
            
            print("Name:", name)
            print("Email:", email)
            print("City:", city)
            print("Password:", passward)

        
            return HttpResponseRedirect('/student/register/')
    else:
        form = Registration()
    return render(request,'student/register.html',{'form':form})

