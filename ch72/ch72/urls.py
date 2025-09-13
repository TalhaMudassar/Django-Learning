from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import student_data_fun
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student_data_fun),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)