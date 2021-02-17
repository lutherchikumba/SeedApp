from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from reports.views import report_view


class TestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User(username='onfarm', password='onfarm00')

    def test_home_view_GET(self):
        request = self.factory.get('/trials/home/')
        request.user = self.user
        response = report_view(request)
        self.assertEqual(response.status_code, 200)
