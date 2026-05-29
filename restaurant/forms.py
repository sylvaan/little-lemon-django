from django import forms
from .models import Booking

SLOT_CHOICES = [
    (10, "10:00 AM"),
    (11, "11:00 AM"),
    (12, "12:00 PM"),
    (13, "01:00 PM"),
    (14, "02:00 PM"),
    (15, "03:00 PM"),
    (16, "04:00 PM"),
    (17, "05:00 PM"),
    (18, "06:00 PM"),
    (19, "07:00 PM"),
    (20, "08:00 PM"),
    (21, "09:00 PM"),
    (22, "10:00 PM"),
]

class BookingForm(forms.ModelForm):
    reservation_slot = forms.ChoiceField(
        choices=SLOT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_slot']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
