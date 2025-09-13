from django.shortcuts import render
from asgiref.sync import sync_to_async,async_to_sync
from django.http import JsonResponse
from core.models import Student
# Create your views here.

# def my_sync_function1(x):
#     return x * 2

# async def my_async_function(x):
#     result = await sync_to_async(my_sync_function1)(5)
#     print(result)


#ASYNCRONOUS FUNCTION to sync
# async def my_async_function(x):
#     return x * 2

# def my_sync_function(x):
#     result = async_to_sync(my_async_function)(5)
#     print(result)




def get_student_data():
    return list(Student.objects.filter(age=20).values())

async def student_data_fun(request):
    student_data = await sync_to_async(get_student_data)()
    return JsonResponse({'data': student_data})