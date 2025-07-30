from django import forms
from .models import Course
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'instructor': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'price': forms.NumberInput(attrs={'class':'form-control','type': 'number', 'placeholder': 'Euro'}),

        }