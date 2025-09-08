from django.shortcuts import render
from school.forms import StudentRegistration,teacher_Registration

# Create your views here.

def student_form_view(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    else:
        form = StudentRegistration()
    return render(request,'school/studentreg.html',{'form':form})

def teacher_from_view(request):
    if request.method == 'POST':
        form = teacher_Registration(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    
    else:
        form = teacher_Registration()
    return render(request,'school/teacherreg.html',{'form':form})
    