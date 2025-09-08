from django.urls import path
from student.views import registration,loginpage
urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', loginpage, name='login'),
]
