from django.shortcuts import render
from datetime import datetime, timedelta


#example 1.1   -variable
# def djagno_learning(req):
#     return render(req,'course\django.html',context={'name':'django '})

#example 1.2 -variable
# def djagno_learning(req):
#     name = 'django'
#     duration = '4 month'
#     seat = 10
#     course_detail = {
#         'name':name,
#         'duration':duration,
#         'seat':seat
        
#     }
#     return render(req,'course\django.html',context=course_detail)

#example 1.3 -filters

# def djagno_learning(req):
#     name = 'django'
#     duration = '4 month'
#     seat = 10
#     string1 = "here are very long string, just for practice on it and learn how djagno treat with strings "

#     # current date
#     current_date = datetime.now()

#     # For timesince and timeuntil
#     post_date = current_date - timedelta(days=3, hours=4)
#     event_date = current_date + timedelta(days=5)

#     # For add, floatformat, pluralize
#     price = 50
#     count = 3
#     float_price = 123.456

#     # For divisibleby and yesno
#     counter = 4
#     is_active = True

#     # For join and slice
#     courses = ['Python', 'Django', 'JavaScript']

#     # For safe and escape
#     html_content = "<b>Hello Django</b>"
    
#     vari = "djangO"

#     course_detail = {
#         'name': name,
#         'duration': duration,
#         'seat': seat,
#         'string1': string1,
#         'current_date': current_date,
#         'post_date': post_date,
#         'event_date': event_date,
#         'price': price,
#         'count': count,
#         'float_price': float_price,
#         'counter': counter,
#         'is_active': is_active,
#         'courses': courses,
#         'html_content': html_content,
#         'vari':vari
#     }
#     return render(req, 'course/django.html', context=course_detail)

# def djagno_learning(req):
#     #doing list for loop
#     list_1 = {"names" : ["math","computer","science","biology"]}
    
#     return render(req,'course\django.html',context=list_1)
    
 #example 8   
# def djagno_learning(req):
#     stu = {
#         'stu1': {'name': 'Rahul', 'roll': 101},
#         'stu2': {'name': 'Sonam', 'roll': 102},
#         'stu3': {'name': 'Raj', 'roll': 103},
#         'stu4': {'name': 'Anu', 'roll': 104},
#     }
#     students = {'student': stu}
#     return render(req, 'course/django.html', context=students)


#example     
# def djagno_learning(req):
#     stu = {
#         'stu1': {'name': 'Rahul', 'roll': 101},

#     }

#     return render(req, 'course/django.html', context={'students':stu})

 #example 10  
def djagno_learning(req):
    stu = {
        'stu1': {'name': 'Rahul', 'roll': 101},
        'stu2': {'name': 'Sonam', 'roll': 102},
        'stu3': {'name': 'Raj', 'roll': 103},
        'stu4': {'name': 'Anu', 'roll': 104},
    }
    students = {'student': stu}
    return render(req, 'course/django.html', context=students)
