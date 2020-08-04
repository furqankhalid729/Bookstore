from django.test import TestCase,client
from .models import book
from django.urls import reverse
# Create your tests here.


class Booktest(TestCase):

    def setUp(self):
        self.book=book.objects.create(
            Name='Django for Professionals',
            author='William S.Vincent',
            Price='39.00'

        )

    def test_book_list(self):
        response=self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/book_list.html')
