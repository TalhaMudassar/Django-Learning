from django import forms

class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    
    # Django automatically:
    # - Converts snake_case → "First name"
    # - CharField → <input type="text">
    # - EmailField → <input type="email">


class login(forms.Form):
    email = forms.EmailField()
    passward = forms.CharField()
