from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'student/home.html')


# def profile(request,my_id):
#     student = {'id':my_id}
#     return render(request,'student/profile.html',student)


# def profile(request,my_class,my_id):
#     student = {'class':my_class,'id':my_id}
#     return render(request,'student/profile.html',student)

def profile(request,year):
    student = {'year':year}
    return render(request,'student/profile.html',student)