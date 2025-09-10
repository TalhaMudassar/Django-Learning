from django.shortcuts import render
from school.models import Student
from django.db.models import Avg,Min,Max,Count,Sum
# Create your views here.
def home(request):
    student_data = Student.objects.all()
    
    
    average = student_data.aggregate(Avg('marks')) 
    
    sum = student_data.aggregate(Sum('marks'))
    
    min = student_data.aggregate(Min('marks'))
    
    MMax = student_data.aggregate(Max('marks'))
    
    count_ = student_data.aggregate(Count('marks'))
    
    context = {'students':student_data,'average':average,'total':sum,'minimum':min,'maximum':MMax,'totalcount':count_}
    

    return render(request,'school/home.html',context)
