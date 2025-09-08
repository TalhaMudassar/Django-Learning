from django.shortcuts import render
from datetime import datetime, timedelta

def djagno_learning(req):
    # Example Data (we will use in template)
    name = 'django'
    duration = '4 month'
    seat = 10
    string1 = "This is a long string for practicing truncatechars filter and others."

    # Current date & time
    current_date = datetime.now()

    # Timesince & timeuntil examples
    post_date = current_date - timedelta(days=3, hours=4)   # 3 days ago
    event_date = current_date + timedelta(days=5, hours=2)  # 5 days in future

    # Numeric data for add, floatformat, pluralize
    price = 50
    count = 3
    float_price = 123.456

    # Divisibleby & yesno
    counter = 4
    is_active = True

    # Lists for join, slice, and for loop
    courses = ['Python', 'Django', 'JavaScript']
    names = ["Math", "Computer", "Science", "Biology"]

    # Safe & escape filters
    html_content = "<b>Hello Django</b>"

    # Variable for if/elif/else condition
    vari = "django"

    # Nested dictionary for looping through key, value
    students = {
        'stu1': {'name': 'Rahul', 'roll': 101},
        'stu2': {'name': 'Sonam', 'roll': 102},
        'stu3': {'name': 'Raj', 'roll': 103},
        'stu4': {'name': 'Anu', 'roll': 104},
    }

    # Passing all data to template
    context = {
        'name': name,
        'duration': duration,
        'seat': seat,
        'string1': string1,
        'current_date': current_date,
        'post_date': post_date,
        'event_date': event_date,
        'price': price,
        'count': count,
        'float_price': float_price,
        'counter': counter,
        'is_active': is_active,
        'courses': courses,
        'names': names,
        'html_content': html_content,
        'vari': vari,
        'student': students
    }

    return render(req, 'course/django.html', context)
