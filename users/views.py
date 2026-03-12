from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class RegistrationCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm

class UserLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = EmailAuthenticationForm