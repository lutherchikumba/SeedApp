from django.test import SimpleTestCase
from django.urls import reverse, resolve
from trials.views import home, trials, measurements, products, treatments
class TestUrls(SimpleTestCase):

    def test_dashboard_url_is_resolves(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_trials_url_is_resolves(self):
        url = reverse('trial_name')
        print(resolve(url))
        self.assertEqual(resolve(url).func, trials)
    
    def test_treatments_url_is_resolves(self):
        url = reverse('treatments')
        print(resolve(url))
        self.assertEqual(resolve(url).func, treatments)

    def test_measurements_url_is_resolves(self):
        url = reverse('measurements')
        print(resolve(url))
        self.assertEqual(resolve(url).func, measurements)

    def test_products_url_is_resolves(self):
        url = reverse('product_name')
        print(resolve(url))
        self.assertEqual(resolve(url).func, products)