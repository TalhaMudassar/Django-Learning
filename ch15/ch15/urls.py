from django.urls import path,include

urlpatterns = [
    path('', include('core.urls')),
    path('course/', include('course.urls')),
]
