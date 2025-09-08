from django.shortcuts import render
from student.models import Studentsdata


# All student view
def alldata(req):
    stu = Studentsdata.objects.all()
    print(stu)
    
    return render(req,'student/all.html',{'studentdatastore':stu})




#single student view
def singlestudentdata(req):
    stusingl = Studentsdata.objects.get(pk=1)
    print(stusingl)
    
    return render(req,'student/single.html',{'studentsingle':stusingl})
