from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth app (home/login/register/password reset)
    path('', include('account.urls')),

    # Role-based dashboards
    path('customer/', include('customer.urls')),
    path('seller/', include('seller.urls')),
]
