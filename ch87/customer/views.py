from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomerDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/dashboard.html')
    
class CustomerPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'customer/password_change.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)
        messages.success(self.request,"Password changed successfully. Please log in with your new password.")
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error changing your password. Please try again.")
        return super().form_invalid(form)
