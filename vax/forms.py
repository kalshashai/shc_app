from django import forms
from django.contrib.admin import widgets
from html5.forms.widgets import DateInput

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
        widgets = {
            'birth_date' : DateInput
        }

class MotherForm(forms.ModelForm):
    class Meta:
        model = Mother
        fields = [
             'first_name', 'middle_name', 'last_name',  'national_id',
            'mobile'
        ]
       
