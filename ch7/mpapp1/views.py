from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request,**kwargs):
    status = kwargs.get('status','None')
    print(status)
    return HttpResponse(f"<h1>Hello from home {status}<h1/>")