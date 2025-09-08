from django.forms import ModelForm
from student.models import Profilee

class ProfileForm(ModelForm):
    class Meta:
        model = Profilee
        fields = ['name', 'email', 'address', 'passward']
