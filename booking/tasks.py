from celery import shared_task
from django.core.mail import send_mail
from config import settings
from django.conf import settings

@shared_task
def send_reservation_confirmation_email(user_email, table, date, time):
    send_mail(
        subject = 'Бронирование подтверждено',
        message = (f'Ваше бронирование подтверждено\n'
                   f'Стол {table}\n'
                   f'Дата {date}\n'
                   f'Время {time}\n'),
        from_email = settings.DEFAULT_FROM_EMAIL,
        recipient_list = [user_email],
        fail_silently=False)
