from django.urls import path
from course.views import learn_django
urlpatterns = [
    path('learning/', learn_django),
]
