from django.urls import path
from student.views import home,registration
urlpatterns = [
    path('', home),
    path('registration/',registration),
   
]
