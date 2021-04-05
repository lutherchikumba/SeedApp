from django import forms
from django.forms import ModelForm
from .models import Grower
from .models import Trial
from .models import Measure
from .models import Product
from .models import CountryList
from .models import ProductList


class Trial_Form(forms.ModelForm):
    latitude = forms.FloatField(error_messages={'required':'Please enter your latitude'})
    longitude = forms.FloatField(error_messages={'required':'Please enter your longitude'})
    crop = forms.CharField(error_messages={'required':'Please enter your crop'})
    notes = forms.CharField(error_messages={'required':'Please enter your notes'})
    user = forms.CharField(error_messages={'required':'Please enter your username'})

    class Meta:
        model = Trial
        fields = ['crop', 'latitude', 'longitude','notes', 'user']

class Grower_Form(forms.ModelForm):
    name = forms.CharField(error_messages={'required':'Please enter your name'})
    email = forms.EmailField(error_messages={'required':'Please enter your email'})
    phone = forms.CharField(error_messages={'required':'Please enter your contact'})
    zip_code = forms.IntegerField(error_messages={'required':'Please enter your zipcode'})


    class Meta:
        model = Grower
        fields = ['name','email', 'phone', 'zip_code']

# class Measurements_Form(forms.ModelForm):
#     measure = forms.CharField(error_messages={'required':'Please enter your measure'})
#     unit = forms.CharField(error_messages={'required':'Please enter your unit of measurement'})
#     timing = forms.CharField(error_messages={'required':'Please enter the time'})
#     value = forms.FloatField(error_messages={'required':'Please enter your value of measurement'})
#     treatment = forms.CharField(error_messages={'required':'Please enter your type of measuremet'})


#     class Meta:
#         model = Measure
#         fields = ['measure','unit', 'timing','value', 'type']


class ProductForm(ModelForm):
    treatment = forms.IntegerField(widget = forms.HiddenInput(), required=True)

    class Meta:
        model = Product 
        fields = ['product','rate', 'timing','unit', 'treatment']


class Filters(forms.Form):
    countries = forms.ModelChoiceField(queryset=CountryList.objects.order_by('name'),
                                       to_field_name='name', empty_label="ALL")
    products = forms.ModelChoiceField(queryset=ProductList.objects.order_by('name'),
                                      to_field_name='name', empty_label="ALL")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['countries'].widget.attrs.update({'class': 'wrapper'})
        self.fields['products'].widget.attrs.update({'class': 'wrapper'})
class Measurements_Form(ModelForm):
    treatment = forms.IntegerField(widget = forms.HiddenInput(), required=True)

    class Meta:
        model = Measure 
        fields = ['measure','unit','timing', 'value', 'treatment']
