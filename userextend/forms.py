from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from userextend.models import UserExtend


class UserForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = [
            'first_name',
            'last_name',
            # 'username',
            'email',
            'type',
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['type'].widget.attrs.update({'class': 'form-select'})
        # self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

    def clean(self):
        cleaned_data = self.cleaned_data

        get_email = cleaned_data.get('email')
        check_emails = User.objects.filter(email=get_email)
        if check_emails:
            msg = 'This email is already in use.'
            self.add_error('email', msg)


        return cleaned_data

class AuthenticationNewForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})