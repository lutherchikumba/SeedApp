from django.test import SimpleTestCase
from django.test import TestCase
from django.utils import timezone
from trials.forms import Trial_Form, ProductForm, Grower_Form, Measurements_Form

class TestForms (TestCase):

    # def test_trial_form_valid_data(self):
    #     form_data = {
    #         'crop' : 'maize',
    #         'latitude' :  '42.83557',
    #         'longitude' : '-105.6259',
    #         'country' : 'USA',
    #         'notes' : 'this is a test'
    #     }
    #     form = Trial_Form(data=form_data)
    #     self.assertTrue(form.is_valid())


    def test_trial_form_no_data(self):
        form = Trial_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    # def test_products_form_valid_data(self):
    #     formset = ProductForm({
    #         'form-TOTAL_FORMS': '2',
    #         'form-INITIAL_FORMS': '0',
    #         'form-0-product': 'GSP',
    #         'form-0-timing': 'V1',
    #         'form-0-rate': '1',
    #         'form-0-unit': 'oz/a',
    #         'form-0-treatment': '1',
    #         'form-1-product': 'GSP',
    #         'form-1-timing': 'V2',
    #         'form-1-rate': '2',
    #         'form-1-unit': 'oz/a',
    #         'form-1-treatment': '2'
    #     })
    #     self.assertTrue(formset.is_valid())
    #     self.assertEquals(len(formset.errors), 5)


    def test_product_form_no_data(self):
        form = ProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)


#     # def test_grower_form_no_data(self):
#     #     form = Grower_Form(data={})

#     #     self.assertFalse(form.is_valid())
#     #     self.assertEquals(len(form.errors), 4)

    def test_measurement_form_valid_data(self):
        form = Measurements_Form(data={
            'measure': 'Yeild',
            'unit': 'bu/z',
            'timing': 'Harvesting',
            'value': 20,
            'treatment': '3'
        })

        self.assertTrue(form.is_valid())

    def test_measurement_form_no_data(self):
        form = Measurements_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)