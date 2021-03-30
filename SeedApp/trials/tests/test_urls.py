from django.test import SimpleTestCase
from django.urls import reverse, resolve
from trials.views import home, trials, measurements, products
class TestUrls(SimpleTestCase):

    def test_dashboard_url_is_resolves(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_trials_url_is_resolves(self):
        url = reverse('trial_name', args=[])
        print(resolve(url))
        self.assertEqual(resolve(url).func, trials)

    def test_measurements_url_is_resolves(self):
        url = reverse('measurement_name', args=[59])
        self.assertEqual(url, '/59/measurements/')
        print(resolve(url))
        self.assertEqual(resolve(url).func, measurements)

    def test_products_url_is_resolves(self):
        url = reverse('product_name', args=[59])
        self.assertEqual(url, '/59/products/')
        print(resolve(url))
        self.assertEqual(resolve(url).func, products)