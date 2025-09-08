from django.urls import path
from django.contrib.auth.views import LogoutView
from account.views import (
    home, login_view, register_view, activate_account,
    password_reset_view, password_reset_confirm_view
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),

    # Email activation
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate'),

    # Forgot password
    path('password_reset/', password_reset_view, name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),

    # Logout (POST in template)
    path('logout/', LogoutView.as_view(), name='logout'),
]
