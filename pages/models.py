from django.db import models

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
