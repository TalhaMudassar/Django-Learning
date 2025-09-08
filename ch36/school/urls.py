from django.urls import path
from school.views import student_form_view ,teacher_from_view
urlpatterns = [
    path('stu_reg/', student_form_view),
    path('tec_reg/',teacher_from_view),
]
