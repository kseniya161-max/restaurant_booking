from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Table(models.Model):
    """Модель столики"""
    number = models.PositiveIntegerField(verbose_name='номер стола', unique=True)
    seats = models.PositiveIntegerField(blank=True, null=True, verbose_name='количество мест', validators=[MinValueValidator(1)])
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name='Описание')
    is_active = models.BooleanField(default=True)
    data = models.TimeField(verbose_name='Дата бронирования', unique=True) # на какой день забронировано
    time = models.TimeField(verbose_name='Время бронирования', unique=True)


    def __str__(self):
        return f"Table {self.number} {self.seats} {self.data}"

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', verbose_name='Клиент')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='free')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')
        ordering = ['-date', '-time']
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"


class ContactMessage(models.Model):
    """ Модель для формы обратной связи"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name}"


class PageContent(models.Model):
    """Модель Контента"""

    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
    ]

    page = models.CharField(max_length=20, choices=PAGE_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='pages/', blank=True, null=True)

    class Meta:
        verbose_name = "Контент страницы"
        verbose_name_plural = "Контент Страниц"

    def __str__(self):
        return f"{self.page} - {self.title}"


