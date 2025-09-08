class OneFormToRuleThemAll(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['student_name', 'teacher_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        role = kwargs.pop('role', 'student')  # pass role='teacher' from view
        super().__init__(*args, **kwargs)
        if role == 'student':
            self.fields.pop('teacher_name')
        else:
            self.fields.pop('student_name')
