from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home page')

def trials(request):
    return HttpResponse('Trials Info')

def treatments(request):
    return HttpResponse('Treatments Info')


def measurements(request):
    return HttpResponse('Measurements Info')


