from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "is_staff", "email", "phone")
    search_fields = ("username", "email")
