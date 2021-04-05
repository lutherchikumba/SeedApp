from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.http import HttpResponse
from .models import Grower
from .models import Trial
from .models import Measure
from .models import Product
from .forms import Trial_Form
from .forms import Grower_Form
from .forms import Measurements_Form
from .forms import ProductForm

# Create your views here.
def home(request):
    form = Grower_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'trials/dashboard.html')

def trials(request):
    form = Trial_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form = form.save()
        id = form.trial_id
        return redirect('product_name', pk = id )
    else:
        return render(request, 'trials/trials_info.html')


def products(request, pk):
    template = 'trials/products_info.html'
    product_set = formset_factory(ProductForm)
    data ={'form-TOTAL_FORMS': '2',
           'form-INITIAL_FORMS': '0',
           'form-0-product': '-----',
           'form-0-timing': '------',
           'form-0-rate': '-----',
           'form-0-unit': '------',
           'form-0-treatment': '1',
           'form-1-product': '-----',
           'form-1-timing': '------',
           'form-1-rate': '-----',
           'form-1-unit': '------',
           'form-1-treatment': '2'
           }
    formset = product_set(data)
    context = {'formset': formset, 'num': '2'}

    if request.method == "POST":
        formset = product_set(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form = form.save(False)
                    form.trial_id = Trial.objects.get(pk = pk)
                    form.save()
                    print(form.as_table())
            return redirect('measurement_name', pk = pk)

    return render(request, template, context)

# def measurements(request, pk):
#     form = Measurements_Form(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form = form.save(False)
#         form.trial_id = Trial.objects.get(pk = pk)
#         form.save()
#         return redirect('trial_name')
#     return render(request, 'trials/measurements_info.html')

def measurements(request, pk):
    template = 'trials/measurements_info.html'
    measurement_set = formset_factory(Measurements_Form)
    data ={'form-TOTAL_FORMS': '2',
           'form-INITIAL_FORMS': '0',
           'form-0-measure': '-----',
           'form-0-unit': '------',
           'form-0-timing': '-----',
           'form-0-value': '-----',
           'form-0-treatment': '1',
           'form-1-measure': '-----',
           'form-1-unit': '------',
           'form-1-timing': '-----',
           'form-1-value': '-----',
           'form-1-treatment': '2'
           }
    formset = measurement_set(data)
    context = {'formset': formset, 'num': '2'}

    if request.method == "POST":
        formset = measurement_set(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form = form.save(False)
                    form.trial_id = Trial.objects.get(pk = pk)
                    form.save()
            return redirect('trial_name')

    return render(request, template, context)


