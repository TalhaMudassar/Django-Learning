from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    passward = forms.CharField(widget=forms.PasswordInput)