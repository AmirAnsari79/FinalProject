import random
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from basket.views import *


class TestUrls(SimpleTestCase):
    def test_detail(self):
        url = reverse('basket:basket_detail')
        self.assertEqual(resolve(url).func, detail)

    def test_AddProduct(self):
        url = reverse('basket:AddProduct', args=[random.randint(1, 1000)])
        self.assertEqual(resolve(url).func, AddProduct)

    def test_Basket_remove(self):
        url = reverse('basket:Basket_remove', args=[random.randint(1, 1000)])
        self.assertEqual(resolve(url).func, Basket_remove)


class TestAddForm(SimpleTestCase):
    def test_AddForm(self):
        form = AddForm()
        if 1 < len(form.Number) < 10:
            self.assertTrue(form.is_valid())
        else:
            self.assertFalse(self)


