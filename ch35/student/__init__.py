# student/forms.py
from django import forms
from student.models import Profile

class RegistrationForm(forms.ModelForm):
    # extra field not in model
    conform_passward = forms.CharField(widget=forms.PasswordInput)

    # override a model field to tighten validation and add attrs
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'nameclass', 'placeholder': 'enter your name '})
    )

    class Meta:
        model = Profile
        # you can also use '__all__', then exclude via 'exclude' (but not both together)
        fields = ['name', 'email', 'passward']
        labels = {'name': 'ENTER NAME', 'email': 'Enter Email:', 'passward': 'Enter Passward'}
        error_messages = {
            'email': {'required': 'Email is required'}
        }
        widgets = {
            'passward': forms.PasswordInput(attrs={'class': 'pwdclass'}),
            # name widget also set above via field override; Meta.widgets would apply if not overridden
        }

    def clean(self):
        cleaned = super().clean()
        pwd = cleaned.get('passward')
        cpwd = cleaned.get('conform_passward')
        if pwd and cpwd and pwd != cpwd:
            self.add_error('conform_passward', 'Passwords do not match.')
        return cleaned
# student/views.py
from django.shortcuts import render, redirect, get_object_or_404
from student.forms import RegistrationForm
from student.models import Profile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Typical ModelForm save
            instance = form.save(commit=False)

            # Example place to transform passward (hashing, etc.)
            # from django.contrib.auth.hashers import make_password
            # instance.passward = make_password(instance.passward)

            instance.save()
            # form.save_m2m()  # only needed if there are M2M fields + commit=False
            return redirect('/student/register/')
    else:
        form = RegistrationForm()
    return render(request, 'student/register.html', {'form': form})

def update_profile(request, pk):
    obj = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/student/register/')
    else:
        form = RegistrationForm(instance=obj)
    return render(request, 'student/register.html', {'form': form})

def delete_profile(request, pk):
    obj = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/student/register/')
    return render(request, 'student/confirm_delete.html', {'obj': obj})
<!-- templates/student/register.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Registration</title>
  <style>
    .errorlist { color: crimson; }
    .field { margin-bottom: 12px; }
    label { display:block; font-weight:600; margin-bottom:4px; }
  </style>
</head>
<body>
  <h1>Register (ModelForm)</h1>

  <form method="post" novalidate>
    {% csrf_token %}
    {{ form.non_field_errors }}

    <div class="field">
      {{ form.name.label_tag }} {{ form.name }}
      {{ form.name.errors }}
    </div>

    <div class="field">
      {{ form.email.label_tag }} {{ form.email }}
      {{ form.email.errors }}
    </div>

    <div class="field">
      {{ form.passward.label_tag }} {{ form.passward }}
      {{ form.passward.errors }}
    </div>

    <div class="field">
      <label for="{{ form.conform_passward.id_for_label }}">Confirm Passward</label>
      {{ form.conform_passward }}
      {{ form.conform_passward.errors }}
    </div>

    <button type="submit">Save</button>
  </form>
</body>
</html>
