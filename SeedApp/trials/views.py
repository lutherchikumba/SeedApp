from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'trials/dashboard.html')

def trials(request):
    return render(request,'trials/trials_info.html')

def treatments(request):
    return render(request, 'trials/treatments_info.html')


def measurements(request):
    return render(request, 'trials/measurements_info.html')


