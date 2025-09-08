from django import forms
from account.models import User

class RegistrationForm(forms.ModelForm):
    ROLE_CHOICES = (
        ('customer','Customer'),
        ('seller','Seller'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES,widget=forms.Select)
    
    """
    Simple registration form:
    - email, name from the model
    - password + confirm_password are plain fields here; we hash password in the view
    """
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "name", "password", "confirm_password"]

    # validate that password and confirm_password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        if password and confirm and password != confirm:
            self.add_error('confirm_password', 'Password and Confirm Password do not match.')
        return cleaned_data

    # ensure email uniqueness at the form level
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email


class PasswordResetForm(forms.Form):
    """
    Minimal 'forgot password' form that only requires an email.
    """
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'})
    )

    def clean_email(self):
        """
        Ensure we only proceed if a user with this email actually exists.
        """
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('No account is associated with this email address.')
        return email
