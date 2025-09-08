from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunction(request):
    return HttpResponse('Hello  world') 

def home(request):
    return HttpResponse("here is our home page ")

def learn_math(request):
    a= 10 + 10
    return HttpResponse(a)

def html_tag(request):
    return HttpResponse("<h1>here is our html tag <h1/>")