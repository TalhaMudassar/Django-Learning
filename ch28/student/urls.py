from django.urls import path
from student.views import registration,Adresses,Login

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('address/', Adresses, name='adress'),
    path('login/', Login, name='login'),
]
