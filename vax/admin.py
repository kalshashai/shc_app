from django.contrib import admin
from .models import (
    Vaccine, Mother, Child, Appointment, 
    VaccineAdmin, MotherAdmin, ChildAdmin, AppointmentAdmin )

# Register your models here.

admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(Mother, MotherAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Appointment, AppointmentAdmin)
