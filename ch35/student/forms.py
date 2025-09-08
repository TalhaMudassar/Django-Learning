from django import forms 
from student.models import Profile


class registrationform(forms.ModelForm):
    name = forms.CharField(max_length=50)
    conform_passward = forms.CharField(widget=forms.PasswordInput)
    class Meta:
       model = Profile
    #    fields = ['name','email','passward']
       fields = '__all__'
       labels = {'name':'ENTER NAME','email':'Enter Email:','passward':'Enter Passward'}
       error_messages = {
           'email' : {'required':'Email is required'}
       }
       widgets = {
            'passward':forms.PasswordInput(attrs={'class':'pwdclass'}),
            'name':forms.TextInput(attrs={'class':'nameclass','placeholder':'enter your name '})
        }