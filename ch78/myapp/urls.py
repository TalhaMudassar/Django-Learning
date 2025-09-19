from django.urls import path
from django.views.generic.base import TemplateView
from myapp import views
urlpatterns = [
    path('home/',TemplateView.as_view(template_name='myapp/home.html'), name='home'),
    # path('index/',views.TemplateView.as_view(template_name='myapp/index.html'), name='index'),
    path('about/',views.AboutTemplateView.as_view(),name='about'),
    path('contact/',views.ContactTemplateView.as_view(extra_context={'course':'Python'}),name='contact'),
    path('profile/<int:id>',views.ProfileTemplateView.as_view(),name='profile'),
]
