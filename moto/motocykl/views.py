from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def index(request):
    return render(request, template_name='index.html')


class MotoListView(ListView):
    model = Motorky
    context_object_name = 'moto_list'
    template_name = 'list.html'


class MotoDetailView(DetailView):
    model = Motorky
    context_object_name = 'moto'
    template_name = 'detail.html'

