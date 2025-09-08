from django.shortcuts import render
from student.forms import Profile
from django.http import HttpResponseRedirect
from student.models import Profilee
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = Profile(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            ad = form.cleaned_data['address']
            pw = form.cleaned_data['passward']
            
            # #(save data into DB)
            # User = Profilee(name=nm,email=em,address=ad,passward=pw)
            # User.save()
            
            # #update data into db
            # User = Profilee(id=1,name=nm,email=em,address=ad,passward=pw)
            # User.save()
            
            # #delete data into db
            # User = Profilee(id=1)
            # User.delete()
            
            return HttpResponseRedirect('/student/register/')
    else: 
          
        form = Profile()
    return render(request,'student/register.html',{'form':form})
