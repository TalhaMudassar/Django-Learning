from django.urls import path
from myapp import views
from django.views.generic.base import TemplateView
urlpatterns = [
   path('contact/',views.ContactFormView.as_view(),name='contactForm'),
   path('thank_you/',TemplateView.as_view(template_name='myapp/thank_you.html'),name='thamk_you'),
   path('register/',views.StudentFormView.as_view(),name='register'),
]
