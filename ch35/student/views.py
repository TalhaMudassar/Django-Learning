from django.shortcuts import render
from student.forms import registrationform
from django.http import HttpResponseRedirect
from student.models import Profile
# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        #method 2 for updating :
        obj = Profile.objects.get(pk=2)
        form = registrationform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/register/')  
    else:
        form = registrationform()
    return render(request,'student/register.html',{'form':form})