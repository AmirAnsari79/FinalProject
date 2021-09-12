from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

# Create your tests here.
from core.views import *


class TestUrls(SimpleTestCase):
    def test_Home_Land(self):
        url = reverse('core:home')
        self.assertEqual(resolve(url).func, Home_Land)

    def test_Home_Land_Slug(self):
        url = reverse('core:categories_sort', args=['amir', ])
        self.assertEqual(resolve(url).func, Home_Land)

    def test_product_details(self):
        url = reverse('core:product_details', args=['amir',])
        self.assertEqual(resolve(url).func, Product_Details)
