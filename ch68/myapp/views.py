from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')


def product(request):
  
    return render(request,'myapp/product.html')

def contact(request):

    return render(request,'myapp/contact.html')

    
    