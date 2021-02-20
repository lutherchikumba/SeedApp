from django.shortcuts import render
from trials.models import Grower, Trial, Product, Measure


def reports_view(request):
    template = 'reports/reports.html'
    if request.method == 'POST':
        print('post')
    growers = Grower.objects.all()
    trials = Trial.objects.all()
    products = Product.objects.all()
    measures = Measure.objects.all()
    context = {
        'hello': 'Hello World!',
        'growers': growers,
        'trials': trials,
        'products': products,
        'measures': measures
    }
    return render(request, template, context)


