from django.urls import path
from student.views import (
    getcookie, setcookie, delcookie,
    getsignedcookie, setsignedcookie
)

urlpatterns = [
    path('get/', getcookie, name='getcookie'),           # read cookie
    path('set/', setcookie, name='setcookie'),           # set cookie
    path('del/', delcookie, name='delcookie'),           # delete cookie
    path('getsigned/', getsignedcookie, name='getsignedcookie'),  # read signed cookie
    path('setsigned/', setsignedcookie, name='setsignedcookie'),  # set signed cookie
]
