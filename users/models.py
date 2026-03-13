from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователь"""

    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="Номер телефона"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email or self.username
