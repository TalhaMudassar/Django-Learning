from django.shortcuts import render

# Create your views here.
def learn_djagno(request):
    course_name = {'c_name':'django 5.1'}
    return render(request,'course/django.html',context=course_name)

def learn_fastapi(request):
    seats = 10
    course_name = {'cname' : 'Fast Api','version':'3','st':seats}
    return render(request,'course/fastapi.html',course_name)
