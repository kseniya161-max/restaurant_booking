from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings



class Table(models.Model):
    """Модель столики"""
    number = models.PositiveIntegerField(verbose_name='номер стола', unique=True)
    seats = models.PositiveIntegerField(blank=True, null=True, verbose_name='количество мест', validators=[MinValueValidator(1)])
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name='Описание')
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return f"Table {self.number} {self.seats}"

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'


class Reservation(models.Model):
    """Модель резервации стола"""
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations', verbose_name='Клиент')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations', verbose_name='стол')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    guests = models.PositiveIntegerField(verbose_name='Количество гостей', validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='free')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')
        ordering = ['-date', '-time']
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"





