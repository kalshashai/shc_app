from django.contrib import admin
from .models import Vaccine, Mother, Child, Appointment

# Register your models here.

admin.site.register(Vaccine)
admin.site.register(Mother)
admin.site.register(Child)
admin.site.register(Appointment)
