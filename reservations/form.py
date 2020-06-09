from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = ('time')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = (
            'seat_type',
            'full_name', 'phone_number',
            'email',
            'date',
            'reserved_start_time',
            'reserved_end_time'
            )
        widgets = {
            'date': DateInput(),
            'reserved_start_time': TimeInput(),
            'reserved_end_time': TimeInput()
            }
        exclude = ['status']



