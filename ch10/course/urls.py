from django.urls import path
from course.views import learn_django,learn_fastapi

urlpatterns = [
    path('learning/',learn_django,name="learn_django"),
    path('learning1/',learn_fastapi,name="fastapi")
]
