from django.urls import path
from course import views

urlpatterns = [
    path('dj/',views.learn_django),
    path('py/',views.learn_python),
]
