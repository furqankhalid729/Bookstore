from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .forms import *

# Create your tests here.
class customeusetest(TestCase):

    def setUp(self):
        url=reverse('signup')
        self.response=self.client.get(url)

    def test_user(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'signup.html')

    def test_signup(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,customUserCreationForm)
        self.assertContains(self.response,'csrfmiddlewaretoken')
