from django import forms 
from myapp.models import Students
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)
    
    
class Student_Contact_Form(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','roll','course']
    