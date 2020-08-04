from django.test import TestCase,SimpleTestCase
from django.urls import reverse
# Create your tests here.
class testcaet(SimpleTestCase):
    def setUp(self):
        url=reverse('home')
        self.response=self.client.get(url)

    def test_status_code(self):

        self.assertEqual(self.response.status_code,200)

    def test_template(self):

        self.assertTemplateUsed(self.response,'home.html')

    def test_content(self):
        template=self.client.get('/')
        self.assertContains(self.response,'Book home page')


class aboutcase(TestCase):
    def setUp(self):
        url=reverse('about')
        self.response=self.client.get(url)

    def test_status(self):
        self.assertEqual(self.response.status_code,200)

    def test_tem(self):
        self.assertTemplateUsed(self.response,'about.html')

