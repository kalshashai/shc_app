from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Vaccine, Mother, Child, Appointment
)
from .forms import ChildForm
# Create your views here.
def index(request):
    return render(request, 'vax/index.html',  {})

def child_list(request):
    children = Child.objects.all()
    context = {'children': children}
    return render(request, 'child/list.html',  context)

def child_show(request, id=None):
    child = get_object_or_404(Child, id=id)
    return render(request, 'child/show.html',  {"child": child})

def child_add(request):
    form = ChildForm(request.POST or None)
    if form.is_valid():
        child = form.save(commit = False)
        child.save()
        return redirect('child_list')

    return render(request, 'child/child_form.html',  {"form": form})

def child_edit(request, id=None):
    child = get_object_or_404(Child, id=id)
    form = ChildForm(request.POST or None, instance = child)
    if form.is_valid():
        child = form.save(commit = False)
        child.save()
        return redirect('child_list')

    return render(request, 'child/child_form.html',  {"form": form})

def child_update(request):
    return render(request, 'child/update.html',  {})

def child_delete(request):
    return render(request, 'child/delete.html',  {})

def about(request):
    return render(request, 'vax/about.html', {})



#if request.user.is_authenticated():
#   do something