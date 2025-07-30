from django import forms
from django.contrib.auth.models import User

from enrollment.models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']

        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select',
                'id': 'student-select'
            }),
            'course': forms.Select(attrs={
                'class': 'form-select',
                'id': 'course-select'
            }),
        }