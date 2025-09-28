from django.urls import path,include
from account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegistrationView.as_view(),name='register'),
    path('activate/<str:uidb64>/<str:token>/',views.activate_account,name='activate'),
    path('password_reset/',views.CustomPasswordResetView.as_view(),name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
]
