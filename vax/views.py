from django.http import HttpResponse
from django.shortcuts import render
from .models import (
    Vaccine, Mother, Child, Appointment
)

# Create your views here.
def index(request):
    return render(request, 'vax/index.html',  {})

def child_list(request):
    children = Child.objects.all()
    context = {'children': children}
    return render(request, 'child/list.html',  context)

def child_add(request):
    return render(request, 'child/add.html',  {})

def child_edit(request):
    return render(request, 'child/edit.html',  {})

def child_update(request):
    return render(request, 'child/update.html',  {})

def child_delete(request):
    return render(request, 'child/delete.html',  {})

def about(request):
    return render(request, 'vax/about.html', {})
