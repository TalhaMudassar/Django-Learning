from django.shortcuts import render
from student.forms import Profile
from django.http import HttpResponseRedirect
# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = Profile(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            roll = form.cleaned_data['roll']
            passward = form.cleaned_data['passward']
            
            print(f"Name:",name)
            print(f"Email:",email)
            print(f"roll:",roll)
            print(f"passward:",passward)
            
            return HttpResponseRedirect('/student/register/')
        
    else:
        form = Profile()
    return render(request,'student/register.html',{'form':form})