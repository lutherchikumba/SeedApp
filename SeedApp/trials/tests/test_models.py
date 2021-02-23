# from django.test import TestCase
# from django.utils import timezone
# from trials.forms import Trial_Form, Products_Form, Treatments_Form, Grower_Form, Measurements_Form
# from trials.models import Grower, Trial, Product, Measure, Treatment

# # class TestModels(TestCase):
# #     def create_grower(self, name = 'Luther', email = 'luther@gmail.com', phone = "9999999999", zip_code = 80015):
# #         return Grower.objects.create(name = name, email = email, phone = phone, zip_code = zip_code)

    
# #     def test_grower_creation(self):
# #         grower = self.create_grower()
# #         self.assertTrue(isinstance(grower, Grower))
# #         self.assertEqual(grower.name, 'Lutherr')

# class TestModels(TestCase):
#     def setUp(self):
#         self.grower = Grower.objects.create(
#         name = 'Luther', 
#         email = 'luther@gmail.com',
#         phone = '9999999999' , 
#         zip_code = 80015
#         )

#         self.trial = Trial.objects.create(
#         latitude = 40, 
#         longitude = -110,
#         crop = 'maize' , 
#         date = timezone.now(),
#         notes = 'This a test',
#         user = 'user 1'
#         )

#         self.product = Product.objects.create(
#         product = 'Corn', 
#         timing = 'V7',
#         rate = 4, 
#         rate_unit = 'oz/a',
#         treatment_id = '7'
#         )

#         self.measure = Measure.objects.create(
#         measure = 'yeild', 
#         unit = 'bu/a',
#         timing = 'Harvest' , 
#         value = 120,
#         type = '1'
#         )
    
#         self.treatment = Treatment.objects.create(
#         treatment = 'bug', 
#         unit = 'bu/z',
#         timing = 'V509' , 
#         value = 111,
#         type_of_treatment = 'TT1'
#         )
    
    
#     def test_grower_creation(self):
#         self.assertTrue(isinstance(self.grower, Grower))
#         self.assertEquals(self.grower.name, 'Luther')
#         self.assertEquals(self.grower.email, 'luther@gmail.com')
#         self.assertEquals(self.grower.phone, '9999999999')
#         self.assertEquals(self.grower.zip_code, 80015)

#     def test_trial_creation(self):
#         self.assertTrue(isinstance(self.trial, Trial))
#         self.assertEquals(self.trial.latitude, 40)
#         self.assertEquals(self.trial.longitude, -110)
#         self.assertEquals(self.trial.crop, 'maize')
#         self.assertEquals(self.trial.date, self.trial.date)
#         self.assertEquals(self.trial.notes, 'This a test')
#         self.assertEquals(self.trial.user, 'user 1')

#     def test_product_creation(self):
#         self.assertTrue(isinstance(self.product, Product))
#         self.assertEquals(self.product.product, 'Corn')
#         self.assertEquals(self.product.timing, 'V7')
#         self.assertEquals(self.product.rate, 4)
#         self.assertEquals(self.product.rate_unit, 'oz/a')
#         self.assertEquals(self.product.treatment_id, '7')

#     def test_measure_creation(self):
#         self.assertTrue(isinstance(self.measure, Measure))
#         self.assertEquals(self.measure.measure, 'yeild')
#         self.assertEquals(self.measure.unit, 'bu/a')
#         self.assertEquals(self.measure.timing, 'Harvest')
#         self.assertEquals(self.measure.value,120)
#         self.assertEquals(self.measure.type, '1')

#     def test_treatment_creation(self):
#         self.assertTrue(isinstance(self.treatment, Treatment))
#         self.assertEquals(self.treatment.treatment, 'bug')
#         self.assertEquals(self.treatment.unit, 'bu/z')
#         self.assertEquals(self.treatment.timing, 'V509')
#         self.assertEquals(self.treatment.value, 111)
#         self.assertEquals(self.treatment.type_of_treatment, 'TT1')

    
