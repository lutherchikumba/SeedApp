from django import forms
from django.forms import ModelForm
from .models import *

class Trial_Form(forms.ModelForm):
    latitude = forms.FloatField(error_messages={'required':'Please enter your latitude'})
    longitude = forms.FloatField(error_messages={'required':'Please enter your longitude'})
    crop = forms.CharField(error_messages={'required':'Please enter your crop'})
    date = forms.DateField(error_messages={'required':'Please enter your date'})
    notes = forms.CharField(error_messages={'required':'Please enter your notes'})
    user = forms.CharField(error_messages={'required':'Please enter your username'})

    class Meta:
        model = Trial
        fields = ['crop', 'latitude', 'longitude', 'date', 'notes', 'user']

class Grower_Form(forms.ModelForm):
    name = forms.CharField(error_messages={'required':'Please enter your timing'})
    email = forms.EmailField(error_messages={'required':'Please enter your date'})
    phone = forms.CharField(error_messages={'required':'Please enter your value'})
    zip_code = forms.IntegerField(error_messages={'required':'Please enter your username'})


    class Meta:
        model = Grower
        fields = ['name','email', 'phone', 'zip_code']

class Measurements_Form(forms.ModelForm):
    measure = forms.CharField(error_messages={'required':'Please enter your timing'})
    unit = forms.CharField(error_messages={'required':'Please enter your date'})
    timing = forms.CharField(error_messages={'required':'Please enter your value'})
    value = forms.FloatField(error_messages={'required':'Please enter your username'})
    type = forms.CharField(error_messages={'required':'Please enter your username'})


    class Meta:
        model = Measure
        fields = ['measure','unit', 'timing','value', 'type']

class ProductForm(ModelForm):
    treatment = forms.IntegerField(widget = forms.HiddenInput(), required=True)

    class Meta:
        model = Product 
        fields = '__all__'