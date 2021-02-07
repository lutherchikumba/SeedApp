from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def reports(request):
    return render(request, 'reports/reports.html')

def maps_of_trials(request):
    return render(request, 'reports/map_of_trials.html')

def trial_reports(request):
    return render(request, 'reports/trial_reports.html')

