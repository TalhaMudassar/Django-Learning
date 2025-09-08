from django.urls import path
from course.views import djagno_learning

urlpatterns = [
    path('learn/', djagno_learning,name="djagno_learning"),
]
