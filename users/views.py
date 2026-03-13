from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from users.models import User
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm


class RegistrationCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = EmailAuthenticationForm
