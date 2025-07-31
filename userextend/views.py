import datetime
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView

from OnlineLearning.settings import EMAIL_HOST_USER
from userextend.forms import UserForm
from userextend.models import UserExtend


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserForm
    success_url = '/login/'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        context['current_datetime'] = now
        return context


    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.upper()
            new_user.last_name = new_user.last_name.upper()

            new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{random.randint(100000,999999)}'

            new_user.save()

            subject = 'Welcome new user'
            message = f'Hello {new_user.first_name} {new_user.last_name}!\n Your username is {new_user.username}'
            send_mail(subject,message, EMAIL_HOST_USER, [new_user.email])
        return super(UserCreateView, self).form_valid(form)



