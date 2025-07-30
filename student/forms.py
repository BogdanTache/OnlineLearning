from django import forms
from student.models import Student
from django.core.validators import MinValueValidator, EmailValidator


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
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
                'placeholder': 'example@domain.com'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 18,
                'max': 100
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        get_email = cleaned_data.get('email')
        check_email = Student.objects.filter(email=get_email)
        if check_email:
            msg = 'This email is already in use.'
            self.add_error('email', msg)


        check_fname = cleaned_data.get('first_name')
        check_lname = cleaned_data.get('last_name')
        check_fname_lname = Student.objects.filter(first_name=check_fname, last_name=check_lname)
        if check_fname_lname:
            msg = 'This first name and last name is already in use.'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        check_age = cleaned_data.get('age')
        if check_age < 18:
            msg = 'This age must be at least 18.'
            self.add_error('age', msg)

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '<EMAIL>'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder':'age', 'min': 18, 'max': 100}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }