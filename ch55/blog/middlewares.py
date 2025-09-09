# def my_fun_middleware(get_response):
#     print("One time Initialiazation")  # her e we write only that code that can implements only one time 
    
#     def my_func(request):
#         print("This is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_func


# from django.shortcuts import HttpResponse
# def my_fun_middleware(get_response):
#     print("One time Initialiazation")  # her e we write only that code that can implements only one time 
    
#     def my_func(request):
#         print("This is before view")
#         response = HttpResponse("Response from my_fun middle-ware")
#         print("This is after view")
#         return response
#     return my_func


# from django.shortcuts import HttpResponse,render
# def my_fun_middleware(get_response):
#     print("One time Initialiazation")  
    
    
#     def my_func(request):
#         print("This is before view")
#         response = render(request,'blog/ui.html') # now here we direct move to html 
#         print("This is after view")
#         return response
#     return my_func


# this can excute accourding to middleware like 1st middleware execute first and than go on 
# class MyClMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print("one time intialization")
        
#     def __call__(self,request):
#         print("this is before view")
#         response = self.get_response(request)
#         print("this is after view")
#         return response


#Mulitiple middleware work

# class MyMiddleware1:
#  def __init__(self, get_response):
#   self.get_response = get_response
#   print("One Time MyMiddleware1 Initialization")

#  def __call__(self, request):
#   print("This is MyMiddleware1 before view")
#   response = self.get_response(request)
#   print("This is MyMiddleware1 after view")
#   return response

# class MyMiddleware2:
#  def __init__(self, get_response):
#   self.get_response = get_response
#   print("One Time MyMiddleware2 Initialization")

#  def __call__(self, request):
#   print("This is MyMiddleware2 before view")
#   response = self.get_response(request)
#   print("This is MyMiddleware2 after view")
#   return response

# class MyMiddleware3:
#  def __init__(self, get_response):
#   self.get_response = get_response
#   print("One Time MyMiddleware3 Initialization")

#  def __call__(self, request):
#   print("This is MyMiddleware3 before view")
#   response = self.get_response(request)
#   print("This is MyMiddleware3 after view")
#   return response


#hooks

# class MyprocessMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
        
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
    
#     def process_view(request,*args,**kwargs):
#         print("This is process view - Before view")
#         return None


# from django.shortcuts import HttpResponse
# class MyExceptionMiddleWare:
#     def __init__(self,get_response):
#         self.get_response = get_response
    
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
    
#     def process_exception(self,request,exception):
#         print("Exception Occured")
#         msg = exception
#         class_name = exception.__class__.__name__
#         print(class_name)
#         print(msg)
#         return HttpResponse(msg)



class MyTemplateResponseMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)
    return response

  def process_template_response(self, request, response):
    print("Process Template Response From Middleware")
    response.context_data['name'] = 'Sonam'
    return response
        
        