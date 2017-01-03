from django.db import models
from django.contrib import admin


# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    month = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name','month', 'timestamp', 'updated')




class Mother(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    national_id = models.CharField(max_length=11, blank=False, null=False)
    mobile = models.CharField(max_length=12, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def fullname(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('mother_show', kwargs={'pk': self.pk})

class MotherAdmin(admin.ModelAdmin):
    list_display = ('fullname','national_id', 'mobile')




class Child(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    ACTIVE = 'AC'
    DECEASED = 'DC'
    DISABLED = 'DI'
    STATUS = (
        (ACTIVE,'Active'),
        (DECEASED, 'Deceased'),
        (DISABLED, 'Disabled')
    )
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    national_id = models.CharField(max_length=11, blank=False, null=False, unique=True)
    MRN = models.CharField(max_length=20, blank=True, null=True, unique=True )
    file_no = models.CharField(max_length=11, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=False, null=False)
    gender = models.CharField(max_length =2, choices = GENDER, default = MALE)
    birth_date = models.DateField()
    status = models.CharField(max_length=2, blank=True, null=True, choices= STATUS)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    mother = models.ForeignKey('Mother', on_delete=models.CASCADE)

    editable_fields = ['first_name', 'middle_name', 'last_name', 'national_id', 'MRN',
                        'file_no', 'nationality', 'gender', 'birth_date', 'status', 'mother']
    
    def my_fields(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in self._meta.fields]

    def fullname(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('child_show', kwargs={'pk': self.pk})

class ChildAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'national_id', 'nationality', 'birth_date')




class Appointment(models.Model):
    VACCINATION = 'V'
    FOLLOWUP = 'F'
    CHECKUP = 'C'
    APP_TYPE = (
        (VACCINATION, 'Vaccination'),
        (FOLLOWUP, 'Follow Up'),
        (CHECKUP, 'Check Up')
    )

    PLANNED = 'P'
    POSTPONED = 'S'
    CANCELLED = 'C'
    ATTENDED = 'A'
    APP_STATUS = (
        (PLANNED, 'Planned'),
        (POSTPONED, 'Postponed'),
        (CANCELLED, 'Cancelled'),
        (ATTENDED, 'Attended')
    )
    ap_date = models.DateTimeField()
    ap_type = models.CharField(max_length=2, blank=True, null=True, choices= APP_TYPE, default= VACCINATION)
    ap_status = models.CharField(max_length=2, blank=True, null=True, choices= APP_STATUS, default= PLANNED)
    ap_report = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    vaccine = models.ForeignKey('Vaccine', on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self):
        return self.child.fullname

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('ap_date', 'child', 'ap_type','ap_status','timestamp','updated')




class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('ap_date', 'child', 'ap_type', 'ap_status', 'updated' )






   
