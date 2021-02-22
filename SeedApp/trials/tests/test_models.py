from django.test import TestCase
from django.utils import timezone
from trials.forms import Trial_Form, Products_Form, Treatments_Form, Grower_Form, Measurements_Form
from trials.models import Grower, Trial, Product, Measure, Treatment

# class TestModels(TestCase):
#     def create_grower(self, name = 'Luther', email = 'luther@gmail.com', phone = "9999999999", zip_code = 80015):
#         return Grower.objects.create(name = name, email = email, phone = phone, zip_code = zip_code)

    
#     def test_grower_creation(self):
#         grower = self.create_grower()
#         self.assertTrue(isinstance(grower, Grower))
#         self.assertEqual(grower.name, 'Lutherr')

class TestModels(TestCase):
    def setUp(self):
        self.grower = Grower.objects.create(
        name = 'Luther', 
        email = 'luther@gmail.com',
        phone = '9999999999' , 
        zip_code = 80015
        )

        self.trial = Trial.objects.create(
        latitude = 40, 
        longitude = -110,
        crop = 'maize' , 
        date = timezone.now(),
        notes = 'This a test',
        user = 'user 1'
        )

        self.product = Product.objects.create(
        product = 'Luther', 
        timing = 'luther@gmail.com',
        phone = '9999999999' , 
        zip_code = 80015
        )

        self.grower = Grower.objects.create(
        name = 'Luther', 
        email = 'luther@gmail.com',
        phone = '9999999999' , 
        zip_code = 80015
        )
    
        self.grower = Grower.objects.create(
        name = 'Luther', 
        email = 'luther@gmail.com',
        phone = '9999999999' , 
        zip_code = 80015
        )
    
    
    def test_grower_creation(self):
        self.assertTrue(isinstance(self.grower, Grower))
        self.assertEquals(self.grower.name, 'Luther')

    
