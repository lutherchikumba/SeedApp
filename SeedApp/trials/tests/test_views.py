from django.test import TestCase, Client
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.forms import UserCreationForm
from trials.models import Grower, Trial, Product, Measure
from trials.forms import Grower_Form
from trials.views import *
import json

class TestViews (TestCase):
    
    def setUp(self):
        self.client = Client()
        self.dashboard_url = reverse('dashboard')
        self.trials_url = reverse('trial_name')
        self.measurements_url = reverse('measurement_name', args=[59])
        self.products_url = reverse('product_name', args=[59])
        self.trial_1 = Trial.objects.create(
            latitude = 42.83557,
            longitude = -105.6259,
            country = 'USA',
            crop = 'maize',
            notes = 'this is a test'
        )

        self.measurements_1 = Measure.objects.create(
            measure = 'Yeild',
            unit =' oz/a',
            timing = 'Harvesting',
            value = '12',
            treatment = 1
        )

    def test_project_home_GET(self):
        form = Trial_Form(data={})
        response = self.client.get(self.dashboard_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trials/dashboard.html')

    def test_project_trials_GET(self):
        form = Trial_Form(data={})
        response = self.client.get(self.trials_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trials/trials_info.html')

    def test_trials_POST_add_new_trial(self):
        Trial.objects.create(
            latitude = 42.83557,
            longitude = -105.6259,
            country = 'USA',
            crop = 'maize',
            notes = 'this is a test'
        )

        response = self.client.post(self.trials_url, {
            'latitude' :  42.83557,
            'longitude' : -105.6259,
            'crop' : 'maize',
            'notes' : 'this is a test',
            'country' : 'USA'
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.trial_1.latitude,  42.83557)
        self.assertEquals(self.trial_1.longitude, -105.6259)
        self.assertEquals(self.trial_1.crop, 'maize')
        self.assertEquals(self.trial_1.notes, 'this is a test')
        self.assertEquals(self.trial_1.country, 'USA')



    def test_measurement_GET(self):

        response_one = self.client.get(self.measurements_url, follow=True)

        self.assertEquals(response_one.status_code, 200)
        self.assertTemplateUsed(response_one, 'trials/measurements_info.html')
        # self.assertRedirects(response_two, 'trials/trials_info.html', status_code=302,fetch_redirect_response=True)

    def test_project_products_GET(self):

        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,  'trials/products_info.html')