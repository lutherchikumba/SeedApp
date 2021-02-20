from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from reports.views import reports_view


class TestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_reports_view_GET(self):
        request = self.factory.get('/reports/')
        request.user = AnonymousUser()
        response = reports_view(request)
        self.assertEqual(response.status_code, 200)

    def test_reports_view_POST(self):
        request = self.factory.post('/reports/')
        request.user = AnonymousUser()
        response = reports_view(request)
        self.assertEqual(response.status_code, 200)
