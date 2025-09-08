from django.urls import path
from student.views import register,success
urlpatterns = [
    path('register/', register),
    path('success/',success),
    
]