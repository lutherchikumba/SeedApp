from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    form = Grower_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'trials/dashboard.html')

def trials(request):
    form = Trial_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'trials/trials_info.html')

def measurements(request):
    form = Measurements_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'trials/measurements_info.html')


# def products(request):
#     products_infor = Product.objects.all()
#     treatments_info = Treatment.objects.all()
#     form = Products_Form(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()

#     return render(request, 'trials/products_info.html', {"Products": products_infor, "Treatment":treatments_info})
    
def treatments(request):
    form = Treatments_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'trials/treatments_info.html')

def products(request):
    template = 'trials/products_info.html'
    product_set = formset_factory(ProductForm)
    data ={'form-TOTAL_FORMS': '2',
           'form-INITIAL_FORMS': '0',
           'form-0-name': '-----',
           'form-0-hybrid': '------',
           'form-0-treatment': '1',
           'form-1-name': '-----',
           'form-1-hybrid': '------',
           'form-1-treatment': '2'}
    formset = product_set(data)
    context = {'formset': formset, 'num': '2'}

    if request.method == "POST":
        formset = product_set(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    print('ok')

    return render(request, template, context)



