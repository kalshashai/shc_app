from django import forms

from .models import (
    Vaccine, Mother, Child, Appointment
)

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = [
            'first_name', 'middle_name', 'last_name',  'national_id',
            'MRN', 'file_no', 'nationality', 'gender', 'birth_date',
            'status', 'mother',
        ]
