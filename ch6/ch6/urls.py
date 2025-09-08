"""
URL configuration for ch6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from app1 import views as ap1
from app2 import views as ap2

from app1.views import home,myapp1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('myapp1/',myapp1,name="myapp1"),
    path('myapp2/',ap2.myapp2,name="myapp2"),
    path('myapp2_me/',ap2.myapp2_me,name="myapp2_me"), 
]