from django.urls import path
from student.views import course
from student import views
urlpatterns = [
    path('course/', course, name="course"),
    path('clear-cache/', views.clear_cache, name='clear_cache'),
    path('clear-sidebar/', views.clear_sidebar_cache, name='clear_sidebar'),
]

