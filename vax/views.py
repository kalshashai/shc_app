from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from html5.forms.widgets import DateInput

from .models import (
    Vaccine, Mother, Child, Appointment
)
from .forms import ChildForm, MotherForm
# Create your views here.
def index(request):
    return render(request, 'vax/index.html',  {})

#Child============================================
class ChildList(ListView):
    model = Child
    context_object_name = 'children'
    template_name='child/list.html'

class ChildDetail(DetailView):
    model = Child
    template_name='child/show.html'

class ChildCreate(CreateView):
    form_class = ChildForm
    model = Child
    template_name='child/child_form.html'

class ChildUpdate(UpdateView):
    model = Child
    form_class = ChildForm
    template_name='child/child_form.html'
    
class ChildDelete(DeleteView):
    model = Child
    success_url = reverse_lazy('child_list')
#End Child==========================================

#Mother=============================================
class MotherList(ListView):
    model = Mother
    context_object_name = 'mothers'
    template_name='mother/list.html'

class MotherDetail(DetailView):
    model = Mother
    template_name='Mother/show.html'

class MotherCreate(CreateView):
    form_class = MotherForm
    model = Mother
    template_name='mother/mother_form.html'

class MotherUpdate(UpdateView):
    model = Mother
    form_class = MotherForm
    template_name='mother/mother_form.html'
    
class MotherDelete(DeleteView):
    model = Mother
    success_url = reverse_lazy('Mother_list')

#End Mother=========================================

def about(request):
    return render(request, 'vax/about.html', {})



#if request.user.is_authenticated():
#   do something