from django.urls import path
from student import views
urlpatterns = [
    path('set/', views.setsession),
    path('get/', views.getsession),
    path('clear/', views.sessionclear),
]