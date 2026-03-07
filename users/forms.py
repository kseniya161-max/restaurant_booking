from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
            self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Имя пользователя'})
            self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Пароль'})
            self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Подтвердите Пароль'})







