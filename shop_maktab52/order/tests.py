import random
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import *


class TestUrls(SimpleTestCase):
    def test_create(self):
        url = reverse('order:create')
        self.assertEqual(resolve(url).func, order_creat)

    def test_payment(self):
        url = reverse('order:payment', args=[random.randint(1, 1000), ])
        self.assertEqual(resolve(url).func, payment)

    def test_detail(self):
        url = reverse('order:detail', args=[random.randint(1, 1000), ])
        self.assertEqual(resolve(url).func, detail)

    def test_coupon_apply(self):
        url = reverse('order:coupon_apply', args=[random.randint(1, 1000), ])
        self.assertEqual(resolve(url).func, coupon_apply)


class TestCouponForm(SimpleTestCase):
    def test_code(self):
        form = CouponForm(data={'code': 'abc'})
        self.assertTrue(form.is_valid())
