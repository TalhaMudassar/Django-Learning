from django import forms

class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    passward = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')
        passward_value = cleaned_data.get('passward')
        if name_value and len(name_value) < 4:
            self.add_error('name','please enter more than 4 character name')
            
        if email_value and not email_value.endswith('@gmail.com'):
            self.add_error('email','please enter @gmail.com')
            
        if passward_value and len(passward_value) < 6:
            self.add_error('passward','please enter atleast 7 digit or higher digits passward')
            
        return cleaned_data
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def clean_name(self):
    #     name_value = self.cleaned_data['name']
    #     if len(name_value) < 4:
    #         raise forms.ValidationError('enter more than 4 or equal to 4 character ')
    #     else:
    #         return name_value
        
    # def clean_email(self):
    #     email_value = self.cleaned_data['email']
    #     if not email_value.endswith('@gmail.com'):
    #         raise forms.ValidationError('please enter @gmail.com')
    #     else:
    #         return email_value
        
     