from django.test import SimpleTestCase
from django.test import TestCase
from django.utils import timezone
from trials.forms import Trial_Form, Products_Form, Treatments_Form, Grower_Form, Measurements_Form

class TestForms (TestCase):

    def test_trial_form_valid_data(self):
        form = Trial_Form(data={
            'latitude': 40,
            'longitude': -110,
            'crop': 'corn',
            'date': timezone.now(),
            'notes': 'This is a test.',
            'user': 'rasMaluda'
        })

        self.assertTrue(form.is_valid())

    def test_trial_form_no_data(self):
        form = Trial_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_products_form_valid_data(self):
        form = Products_Form(data={
            'product': 'GPS',
            'timing': 'V1',
            'rate': 2.1,
            'rate_unit': 'oz/a',
            'treatment_id': '4'
        })

        self.assertTrue(form.is_valid())

    def test_product_form_no_data(self):
        form = Products_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_treatments_form_valid_data(self):
        form = Treatments_Form(data={
            'treatment': 'luther',
            'unit': 'bu/a',
            'timing': 'v56',
            'value': 125,
            'type_of_treatment': 'dell'
        })

        self.assertTrue(form.is_valid())

    def test_treatments_form_no_data(self):
        form = Treatments_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_grower_form_valid_data(self):
        form = Grower_Form(data={
            'name': 'maize',
            'email': 'bu@gmail.com',
            'phone': '9999999999',
            'zip_code': 80015
        })

        self.assertTrue(form.is_valid())

    def test_grower_form_no_data(self):
        form = Grower_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_measurement_form_valid_data(self):
        form = Measurements_Form(data={
            'measure': 'Yeild',
            'unit': 'bu/z',
            'timing': 'Harvesting',
            'value': 20,
            'type': '3'
        })

        self.assertTrue(form.is_valid())

    def test_measurement_form_no_data(self):
        form = Measurements_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)