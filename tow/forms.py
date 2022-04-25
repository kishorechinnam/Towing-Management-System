from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import DateTimeInput

from .models import Vehicles, AllocatedVehicles


class CheckInForm(forms.ModelForm):
    class Meta:
        model = AllocatedVehicles
        fields = ('vehicle_assigned', 'client_assigned', 'allocated_by', 'towing_in_date', 'towing_out_date', 'payment_id')
        widgets = {
            'towing_in_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'towing_out_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(CheckInForm, self).__init__(*args, **kwargs)
        self.fields['vehicle_assigned'].queryset = Vehicles.objects.filter(assigned=False)


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = AllocatedVehicles
        fields = ('towing_out',)
