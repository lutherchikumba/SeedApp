from django import forms
from django.forms import ModelForm
from .models import Grower
from .models import Trial
from .models import Measure
from .models import Product
from .models import CountryList, ProductList, CropList


class Trial_Form(forms.ModelForm):
    latitude = forms.FloatField(error_messages={'required':'Please enter your latitude'})
    longitude = forms.FloatField(error_messages={'required':'Please enter your longitude'})
    crop = forms.ModelChoiceField(queryset=CropList.objects.order_by('name'),
                           to_field_name='name', empty_label="Select Crop")
    country = forms.ModelChoiceField(queryset=CountryList.objects.order_by('name'),
                                  to_field_name='name', empty_label="Select Country")
    notes = forms.CharField(error_messages={'required':'Please enter your notes'})

    class Meta:
        model = Trial
        fields = ['crop', 'latitude', 'longitude', 'country', 'notes']


class Grower_Form(forms.ModelForm):
    name = forms.CharField(error_messages={'required':'Please enter your name'})
    email = forms.EmailField(error_messages={'required':'Please enter your email'})
    phone = forms.CharField(error_messages={'required':'Please enter your contact'})
    zip_code = forms.IntegerField(error_messages={'required':'Please enter your zipcode'})


    class Meta:
        model = Grower
        fields = ['name','email', 'phone', 'zip_code']   



class ProductForm(ModelForm):
    treatment = forms.IntegerField(widget = forms.HiddenInput(), required=True)
    product = forms.ModelChoiceField(queryset=ProductList.objects.order_by('name'),
                                  to_field_name='name', empty_label="Select Product")
    class Meta:
        model = Product 
        fields = ['product','rate', 'timing','unit', 'treatment']


class Measurements_Form(ModelForm):
    treatment = forms.IntegerField(widget = forms.HiddenInput(), required=True)

    class Meta:
        model = Measure 
        fields = ['measure','unit','timing', 'value', 'treatment']


class Filters(forms.Form):
    countries = forms.ModelChoiceField(queryset=CountryList.objects.order_by('name'),
                                       to_field_name='name', empty_label="ALL")
    crops = forms.ModelChoiceField(queryset=CropList.objects.order_by('name'),
                                       to_field_name='name', empty_label="ALL")
    products = forms.ModelChoiceField(queryset=ProductList.objects.order_by('name'),
                                      to_field_name='name', empty_label="ALL")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['countries'].widget.attrs.update({'class': 'wrapper'})
        self.fields['products'].widget.attrs.update({'class': 'wrapper'})
        self.fields['crops'].widget.attrs.update({'class': 'wrapper'})
