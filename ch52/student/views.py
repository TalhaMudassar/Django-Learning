from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def course(request):
#     mv = cache.get('movie','has_expired') # movie is key. has_expired has value  
#     if mv == 'has_expired':   # here we check for avoid error's
#         cache.set('movie','Harry Potter',60) # movie are key , harrypotter are value and 60 seconds 
#         mv = cache.get('movie')
#     return render(request,'student/course.html',{'mv':mv})


# def course(request):
#     mv = cache.get_or_set('movie','Harry potter',15) 
#     mv1 = cache.get_or_set('movie','The one',15, version=2)  # same key version different
#     print(mv1) 
#     return render(request,'student/course.html',{'mv':mv})

# def course(request):
#     # Correct way: keys are cache keys
#     cache.set_many({'student_name': 'talha', 'student_roll': 100}, 30)

#     # Retrieve using keys (list of cache keys)
#     stu = cache.get_many(['student_name', 'student_roll'])

#     return render(request, 'student/course.html', {'stu': stu})

def course(request):
    cache.delete('movie',version=2)
    return render(request,'student/course.html')

# def course(request):
#     cache.clear()
#     return render(request,'student/course.html')

