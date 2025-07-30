from django import forms

from instructor.models import Instructor


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name...',
                'autofocus': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@company.com'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
            'hire_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'YYYY-MM-DD'
            }),
        }



    def clean(self):

        check_fname = self.cleaned_data.get('first_name')
        check_lname = self.cleaned_data.get('last_name')
        check_fname_lname = Instructor.objects.filter(first_name=check_fname, last_name=check_lname)
        if check_fname_lname:
            msg = 'first_name already exists'
            msg1 = 'last_name already exists'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg1)

        get_email = self.cleaned_data.get('email')
        check_email = Instructor.objects.filter(email=get_email)
        if check_email:
            msg = 'email already exists'
            self.add_error('email', msg)




class InstructorUpdateForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'email', 'course']


        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name...',
                'autofocus': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@company.com'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select'
            }),
        }