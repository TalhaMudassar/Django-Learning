from django import forms

# class Profile(forms.Form):
#     name = forms.CharField(error_messages={'required':'Name is required'})
#     email = forms.EmailField(error_messages={'required':'Email is required'},min_length=5, max_length=50)
#     roll = forms.IntegerField(error_messages={'required':'Roll is required'})
#     passward = forms.CharField(error_messages={'required':'Password is required'},widget=forms.PasswordInput(), min_length=5, max_length=50)
    
  
class Profile(forms.Form):
    error_css_class = 'my error'
    required_css_class = 'required'
    name = forms.CharField(error_messages={'required':'Name is required'})
    email = forms.EmailField(error_messages={'required':'Email is required'},min_length=5, max_length=50)
    roll = forms.IntegerField(error_messages={'required':'Roll is required'})
    passward = forms.CharField(error_messages={'required':'Password is required'},widget=forms.PasswordInput(), min_length=5, max_length=50)
      
    
    