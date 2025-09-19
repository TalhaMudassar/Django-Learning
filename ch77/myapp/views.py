from django.shortcuts import render,HttpResponse
from myapp.forms import ContactForm

from django.views import View  #

# Create your views here.
def myfunview1(request):
    return HttpResponse("Hello Function based view")

class MyClassView1(View):  #in class based view first word name are capital
    #in class based view we need to write a get , but in function based we cannot need that 
    def get(self,request):  
        return HttpResponse("Hello Clased Based View")
        
def myfunview2(request):
    return HttpResponse("<h1> Function Based View </h1>")

class MyClassView2(View):
    def get(self,request):
        return HttpResponse("<h1> Function Based View </h1>")
    
    
class MyClassView3(View):
    data = "pass value through my class view 3"
    def get(self,request):
        return HttpResponse(self.data)
    
#we should also use inhertance 
class MyChildClassView3(MyClassView3):
    def get(self,request):
        return HttpResponse(self.data)

def homefunview(request):
    return render(request,'myapp/home.html')

class HomeClassView(View):
    def get(request,get):
        return render(request,'myapp/home.html')

def aboutfunview(request):
    context = {'msg': 'Welcome to Geeky shows Function Based View'}
    return render(request,'myapp/about.html',context)

class AboutClassView(View):
    def get(self,request):
        context = {'msg': 'Welcome to Geeky shows Function Based View'}
        return render(request,'myapp/about.html',context)
    
# #here is our first view
# def newsfunview(request):
#     template_name = 'myapp/news.html'
#     context = {'info':'Subscribe to Geeky Shows YT Channel'}
#     return render(request,template_name,context)


#here is our second view
def newsfunview(request,template_name):
    template_name = template_name
    context = {'info':'Subscribe to Geeky Shows YT Channel'}
    return render(request,template_name,context)

#inclass
class NewsClassView(View):
    template_name = ''
    def get(self,request):
        context = {'info':'Subscribe to Geeky Shows YT Channel'}
        return render(request,self.template_name,context)

def contactfunview(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data['name'])
        return HttpResponse("Thank you for Submitted")
    else:
        form = ContactForm()
    return render(request,'myapp/contact.html',{'form':form})

class ContactClassView(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'myapp/contact.html',{'form':form})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])  
            return render(request,'myapp/contact.html',{'form':form})
   
       
            
    
    
    