from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myapp2(request):
    return HttpResponse("Hello from my app 2")

def myapp2_me(request):
    return HttpResponse("Hello from myapp2_me")
