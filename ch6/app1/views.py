from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse("Hello from home page")

def myapp1(request):
    return HttpResponse("Hello from my app 1")
 