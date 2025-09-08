from django.urls import path
from student.views import Register
urlpatterns = [
    path('register/', Register),
]
