from django.shortcuts import render
from django.contrib import messages
from student.forms import StudentRegistration
# Create your views here.
def home(request):
    #here is the method 1 to show the messages 
    # messages.add_message(request,messages.SUCCESS,'Your message has been successfully created!')
    # messages.add_message(request,messages.INFO,'Your message contain some information')
    # messages.add_message(request,messages.WARNING,'Your message have some warining ')
    # messages.add_message(request,messages.ERROR,'Your message have some error !')
    
    # Here is the method 2 how we use the message 
    # messages.success(request,'this is success')
    # messages.info(request,'this is info')
    # messages.warning(request,'this is warning')
    # messages.error(request,'this is error')
    # messages.debug(request,'this is debug')
    
    
    # print(messages.get_level(request)) # 20
    # messages.set_level(request,messages.DEBUG)
    # messages.debug(request,'this is debug after set !!! ')
    # print(messages.get_level(request))
    
    
    
    
    return render(request,'student/home.html')


def registration(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Form SuccessFully Submitted!')
    else:   
        fm = StudentRegistration()
    return render(request,'student/registration.html',{'fm':fm})