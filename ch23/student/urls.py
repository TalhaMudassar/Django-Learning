from django.urls import path
from student.views import alldata,singlestudentdata

urlpatterns = [
    path('all/', alldata),
    path('single/', singlestudentdata),
]