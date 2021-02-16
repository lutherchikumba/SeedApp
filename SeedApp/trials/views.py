from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'trials/dashboard.html')

def trials(request):
    form = Trial_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'trials/trials_info.html')


def treatments(request):
    return render(request, 'trials/treatments_info.html')


def measurements(request):
    form = Measurements_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'trials/measurements_info.html')


def products(request):
    form = Products_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'trials/products_info.html')
    




