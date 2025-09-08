from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'data':'Hello i am django developer. i am also creating educational videos. i am not human '}
    
    return render(request,'student/home.html',context)
