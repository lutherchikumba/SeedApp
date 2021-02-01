from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def reports(request):
    return HttpResponse('Reports Info')

def maps_of_trials(request):
    return HttpResponse('Map Of Trials')

def trial_reports(request):
    return HttpResponse('Trial Report')

