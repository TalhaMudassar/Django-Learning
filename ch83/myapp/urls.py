from django.urls import path
from myapp import views
from django.views.generic.base import TemplateView
urlpatterns = [
    # path('create/',views.StudentCreateView.as_view(),name='studentcreate'),
    path('thanks/',TemplateView.as_view(template_name = 'myapp/thanks.html'),name='thanks'),
    
    path('register/',views.StudentCreateView.as_view(),name='register'),
]
