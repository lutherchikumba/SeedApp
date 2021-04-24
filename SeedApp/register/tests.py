from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


# class BaseTest(TestCase):
#     def setUp(self):
#         self.register_url = reverse('register')


#         return super().setUp()

# class RegisterTest(BaseTest):
#     def test_can_view_page_correctly(self):
#         response = self.client.get(self.register_url)
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response='login')  