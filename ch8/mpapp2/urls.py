from django.urls import path
from mpapp2 import views as pt2

urlpatterns = [
    path('myapp2/',pt2.myapp2,name='myapp2'),
  
]