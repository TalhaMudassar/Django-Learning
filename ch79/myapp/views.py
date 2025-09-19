from django.shortcuts import render
from django.views.generic.base  import RedirectView
# Create your views here.


class NewClassView(RedirectView):
    # url = "/"
    # pattern_name='home'   #here we also pass pattern_name
    url = 'http://google.com'       # here we also pass the external link
    
    
class SuccessClassView(RedirectView):
    pattern_name = 'profile'
    query_string= True
    
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)