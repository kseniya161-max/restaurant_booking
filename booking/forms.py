from django.forms import ModelForm, forms
from booking.models import Reservation


class ReservationForm(forms,ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'guests']


    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get("table")
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if Reservation.objects.filter(
            table = table,
            date = date,
            time = time,
            status = 'confirmed'
        ).exists():
            raise forms.ValidationError('Этот стол уже забронирован')
        return cleaned_data



    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['table'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите номер стола'})
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите время'})
        self.fields['guests'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите количество гостей'})



