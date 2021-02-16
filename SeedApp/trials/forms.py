from django import forms
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
        fields = ('crop',)
        fields = ('latitude',)
        fields = ('longitude',)
        fields = ('date',)
        fields = ('notes',)
        fields = ('user',)

class Products_Form(forms.ModelForm):
    product = forms.CharField(label='product', max_length=100)
    timing = forms.CharField(error_messages={'required':'Please enter your timing'})
    rate = forms.FloatField(error_messages={'required':'Please enter your date'})
    rate_unit = forms.CharField(error_messages={'required':'Please enter your value'})
    # treatment_id = forms.CharField(error_messages={'required':'Please enter your username'})
    class Meta:
        model = Product
        fields = ('product',)
        fields = ('timing',)
        fields = ('rate',)
        fields = ('rate_unit',)
        # fields = ('treatment_id',)

class Measurements_Form(forms.ModelForm):
    measure = forms.CharField(error_messages={'required':'Please enter your product'})
    unit = forms.CharField(error_messages={'required':'Please enter your timing'})
    timimg = forms.CharField(error_messages={'required':'Please enter your date'})
    value = forms.FloatField(error_messages={'required':'Please enter your value'})
    # treatment_id = forms.CharField(error_messages={'required':'Please enter your username'})

    class Meta:
        model = Measure
        fields = ('measure',)
        fields = ('unit',)
        fields = ('timing',)
        fields = ('value',)
        # fields = ('type',)