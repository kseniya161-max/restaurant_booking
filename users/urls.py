from django.urls import path

from users.views import RegistrationCreateView

app_name = "users"

urlpatterns = [
    path("register/", RegistrationCreateView.as_view(), name="register"),
]