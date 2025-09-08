from django.urls import path
from student.views import demofiles
urlpatterns = [
    path('form/', demofiles),
    
]
