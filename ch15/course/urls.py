from django.urls import path
from course.views import learn_django,learn_python

urlpatterns = [
    path('djnagolearning/', learn_django),
    path('pythonlearning/',learn_python),
]