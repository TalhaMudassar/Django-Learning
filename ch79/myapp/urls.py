from django.urls import path,include
from django.views.generic.base  import TemplateView,RedirectView
from myapp import views
urlpatterns = [
    path('', TemplateView.as_view(template_name='myapp/home.html'),name='home'),
    path('home/', RedirectView.as_view(url='/'),name='home1'),
    # path('index/', views.RedirectView.as_view(url='/'),name='index'),
    path('index/', views.RedirectView.as_view(pattern_name='home'),name='index'),
    path('newhome/', views.NewClassView.as_view(),name='newhome'),
    
    
    path('profile/<int:id>', TemplateView.as_view(template_name='myapp/profile.html'),name='profile'),
    path('login/', TemplateView.as_view(template_name='myapp/login.html'),name='login'),
    path('success/<int:id>', views.SuccessClassView.as_view(),name='success'),
]

