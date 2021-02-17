from django.shortcuts import render
from trials.models import Grower, Trial, Product, Measure


def reports_view(request):
    template = 'reports/reports.html'
    context = {
        'hello': 'hello'
    }
    return render(request, template, context)


