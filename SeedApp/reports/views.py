from django.shortcuts import render
from trials.models import Grower, Trial, Product, Measure
from django.core.serializers import serialize


def reports_view(request):
    template = 'reports/reports.html'
    if request.method == 'POST':
        print('post')

    trials = serialize('json', Trial.objects.all())
    print(trials)
    context = {
        'trials': trials,
    }
    return render(request, template, context)


