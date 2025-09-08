from django import forms

class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(initial='ali alli')
    email = forms.EmailField()
    city = forms.CharField()
    
    
class Adress(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()
    
    
class login(forms.Form):
    name = forms.CharField()
    passward = forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput())
    
    
