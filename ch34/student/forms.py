from django import forms

class Profile(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    passward = forms.CharField(widget=forms.PasswordInput)
    
    
    