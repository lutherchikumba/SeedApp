from django.shortcuts import render
from trials.models import Grower, Trial, Product, Measure
from trials.forms import Filters
import json


def reports_view(request):
    template = 'reports/reports.html'
    form = Filters()
    if request.method == 'POST':
        print('post')

    trials = Trial.objects.all()
    measures = Measure.objects.all()
    products = Product.objects.all()
    data = []
    for trial in trials:
        trial_measures = list(measures.filter(trial_id=trial.trial_id).values())
        trial_products = list(products.filter(trial_id=trial.trial_id).values())
        data.append({'id': trial.trial_id,
                                'crop': trial.crop,
                                'lat': trial.latitude,
                                'lng': trial.longitude,
                                'measures': trial_measures,
                                'products': trial_products})
    data = json.dumps(data)
    context = {
        'data': data,
        'form': form,
    }
    return render(request, template, context)


