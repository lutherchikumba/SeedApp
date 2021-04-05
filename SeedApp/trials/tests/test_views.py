from django.test import TestCase, Client
from django.urls import reverse
from django.test import RequestFactory
from trials.models import Grower, Trial, Product, Measure
import json

class TestViews (TestCase):
    
    def setUp(self):
        self.client = Client()
        self.dashboard_url = reverse('dashboard')
        self.trials_url = reverse('trial_name')
        self.measurements_url = reverse('measurement_name', args=[59])
        self.products_url = reverse('product_name', args=[59])

    def test_project_home_GET(self):

        response = self.client.get(self.dashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trials/dashboard.html')


        response = self.client.get(self.dashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trials/dashboard.html')

    def test_project_trials_GET(self):

        response = self.client.get(self.trials_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trials/trials_info.html')

    def test_project_measurement_GET(self):

        response = self.client.get(self.measurements_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trials/measurements_info.html')
        # self.assertRedirects(response, 'trial_name')

    def test_project_products_GET(self):

        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,  'trials/products_info.html')


