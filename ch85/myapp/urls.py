from django.urls import path
from myapp import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('delete/<int:pk>', views.StudentDeleteView.as_view(),name='studelete'),
    path('success/',TemplateView.as_view(template_name='myapp/success.html'),name='success')

]
