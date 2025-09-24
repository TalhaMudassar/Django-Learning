from django.urls import path
from myapp import views
from django.views.generic.base import TemplateView
urlpatterns = [
    # path('update/<int:pk>', views.StudentUpdateView.as_view(),name='update'),  # during update view use it demand's slug or pk
    path('update/<int:pk>', views.StudentUpdateView.as_view(),name='update'),
    path('thanks/',TemplateView.as_view(template_name = 'myapp/thankyou.html'),name='thanks')
]
