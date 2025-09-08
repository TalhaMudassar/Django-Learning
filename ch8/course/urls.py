from django.urls import path
from course.views import learn_python

urlpatterns = [
   path('python/',learn_python,name='myapp2'),
]