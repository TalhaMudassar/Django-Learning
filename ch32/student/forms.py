from django import forms
from django.core import validators

def start_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('email should start with s ')

class Registration(forms.Form):
    #build in validator
    name = forms.CharField(
        validators=[
            validators.MaxLengthValidator(10),
            validators.MinLengthValidator(3) 
        ]
        )
    # use custom validetor 
    email = forms.EmailField(validators=[start_with_s])
    city = forms.CharField()
    passward = forms.CharField(widget=forms.PasswordInput())