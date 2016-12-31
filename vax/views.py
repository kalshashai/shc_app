from django.http import HttpResponse
from django.shortcuts import render
from .models import (
    Vaccine, Mother, Child, Appointment
)

# Create your views here.
def index(request):
    children = Child.objects.all()
    context = {'children': children}
    return render(request, 'vax/index.html',  context)

def about(request):
    return render(request, 'vax/about.html', {})
