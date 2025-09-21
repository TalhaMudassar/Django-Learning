class StudentListView6(ListView):
    model = Student
    template_name = 'myapp/default.html'

    def get_template_names(self):
        if self.request.COOKIES.get('user') == 'sonam':
            return ['myapp/sonam.html']
        return [self.template_name]
