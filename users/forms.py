from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите email"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите Пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Подтвердите Пароль"}
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EmailAuthenticationForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Введите пароль"}
        ),
    )
