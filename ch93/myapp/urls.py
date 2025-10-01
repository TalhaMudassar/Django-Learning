from django.urls import path
from .views import HomeView, SyncView, AsyncView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sync/', SyncView.as_view(), name='sync_view'),
    path('async/', AsyncView.as_view(), name='async_view'),
]