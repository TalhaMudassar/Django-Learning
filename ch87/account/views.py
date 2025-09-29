from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import FormView 
from account.forms import RegistrationForm,PassswordResetForm
from account.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from django.urls import reverse_lazy
from account.utils import send_activation_email, send_reset_password_email 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm


class HomeView(View):
    def get(self,request, *args,**kwargs):
        return render(request,'account/home.html')
    
class LoginView(View):
    
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_seller:
                return redirect('seller_dashboard')
            elif request.user.is_customer:
                return redirect('customer_dashboard')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args,**kwargs):
        return render(request,'account/login.html')
    
    def post(self,request, *args,**kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #check if email or password are not provided.
        if not email or not password:
            messages.error(request,"Both fields are required")
            return redirect('account:login')
        
        #check if the user exists
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            # if user does not exist so show the error message
            messages.error(request,"invalid password or email")
            return redirect('login')

        # Check if the user is inactive
        if user is not None:
            if not user.is_active:
                messages.error(request,"Your account is inactive. Please activate your account.")
                return redirect('login')
            
            
        # Authenticate user if active
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Log the user in
            login(request, user)

            if user.is_seller:
                return redirect('seller_dashboard')
            
            elif user.is_customer:
                return redirect('customer_dashboard')
            else:
                messages.error(
                    request, "You do not have permission to access this area."
                )
                return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
            
    
    
class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = False # Account inactive until email is verified
        user.save()

        # Send Account Activation Email
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = reverse(
            'activate', kwargs={'uidb64': uidb64, 'token': token})
        activation_url = f'{settings.SITE_DOMAIN}{activation_link}'
        send_activation_email(user.email, activation_url)
        messages.success(
            self.request, 'Registration successful! Please check your email inbox/spam to activate your account.')
        return redirect('login')
    
    


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        # Check the token for one-time use and if the account is already active
        if user.is_active:
            messages.warning(
                request, "This account has already been activated.")
            return redirect('login')

        if default_token_generator.check_token(user, token):
            user.is_active = True  # Activate the account
            user.save()            # Save the updated user
            messages.success(
                request, "Your account has been activated successfully!"
            )
            return redirect('login')
        else:
            messages.error(
                request, "The activation link is invalid or has expired."
            )
            return redirect('login')

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, "Invalid activation link.")
        return redirect('login')
        
    
    
class CustomPasswordResetView(FormView):
    template_name = 'account/password_reset.html'
    form_class = PassswordResetForm
    success_url = reverse_lazy('login')
    success_message = (
        'We have sent you a password reset link. Please check your email.')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            reset_url = self.get_reset_url(user)
            # Send the email only once using your custom function
            send_reset_password_email(user.email, reset_url)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # If form is invalid, pass the error messages to the template
        messages.warning(self.request, (
            'No account with that email exists.'
        ))
        return super().form_invalid(form)
    
    def get_reset_url(self, user):
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_url = reverse_lazy('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        return f"{self.request.build_absolute_uri(reset_url)}"
    
    
class PasswordResetConfirmView(View):
    template_name = 'account/password_reset_confirm.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)

            # Check the token
            if default_token_generator.check_token(user, token):
                form = SetPasswordForm(user=user)
                return render(request, self.template_name, {'form': form, 'uidb64': uidb64, 'token': token})
            else:
                messages.error(request, (
                    'This link has expired or is invalid.'))
                return redirect('password_reset')
        except Exception as e:
            messages.error(request, (
                'An error occurred. Please try again later.'))
            return redirect('password_reset')

    def post(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)

            # Check the token
            if default_token_generator.check_token(user, token):
                form = SetPasswordForm(user=user, data=request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, (
                        'Your password has been successfully reset.'))
                    return redirect('login')
                else:
                    # If form is not valid, add errors to the message framework
                    for field, errors in form.errors.items():
                        for error in errors:
                            # Add each error as a message
                            messages.error(request, error)
                    return render(request, self.template_name, {'form': form, 'uidb64': uidb64, 'token': token})
            else:
                messages.error(request, (
                    'This link has expired or is invalid.'))
                return redirect('password_reset')
        except Exception as e:
            messages.error(request, (
                'An error occurred. Please try again later.'))
            return redirect('password_reset')
    
    
    
    
