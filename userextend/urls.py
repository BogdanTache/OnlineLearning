from django.urls import path

from userextend import views
from userextend.views import UserCreateView

urlpatterns = [
    path('create_user', views.UserCreateView.as_view(), name='create_user'),
]