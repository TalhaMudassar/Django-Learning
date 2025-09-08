from django.urls import path
from mpapp1 import views as pt1

urlpatterns = [
    path('home/',pt1.home,{'status':'OK'},name='home'),
 
]