from django.forms import ModelForm
from booking.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'guests']


    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['table'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите номер стола'})
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите время'})
        self.fields['guests'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите количество гостей'})



