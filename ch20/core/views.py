from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'core/home.html',{'cour':'python latest'})

def about(req):
    return render(req,'core/about.html')


