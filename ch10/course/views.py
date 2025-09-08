from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request, 'course/django.html')

def learn_fastapi(request):
    return render(request, 'course/fastapi.html')
