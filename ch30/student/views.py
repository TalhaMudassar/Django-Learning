from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            passward = form.cleaned_data['passward']
            print(f'Name:',name)
            print(f'Email:',email)
            print(f'City:',city)
            print(F'Passward:',passward)
            return HttpResponseRedirect('/student/success')
        pass
    else:
        form = Registration()
    return render(request,'student/register.html',{'form':form})

def success(req):
    return render(req,'student/success.html')
