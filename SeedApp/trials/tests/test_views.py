from django.test import TestCase, Client
from django.urls import reverse
from .models import *
import json

class TestViews (TestCase):
    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trials/trials_info.html')