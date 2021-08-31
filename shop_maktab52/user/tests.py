from django.test import TestCase, SimpleTestCase, Client
from .views import *
from django.urls import reverse, resolve
from .forms import *
from django.utils.translation import gettext as _


class TestUrls(SimpleTestCase):
    def test_register(self):
        url = reverse('user:register')
        self.assertEqual(resolve(url).func, UserRegister)

    def test_login(self):
        url = reverse('user:login')
        self.assertEqual(resolve(url).func, UserLogin)

    def test_logout(self):
        url = reverse('user:logout')
        self.assertEqual(resolve(url).func, UserLogout)


class TestUserRegistrationForm(SimpleTestCase):
    def test_valid_data(self):
        form = UserRegistrationForm(data={'email': 'amir@gmail.com', 'full_name': 'amir', 'password': '1234'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class TestUserLoginForm(SimpleTestCase):
    def test_valid_data(self):
        form = UserLoginForm(data={'email': 'amir@gmail.com', 'password': '1234'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_UserRegister_GET(self):
        response = self.client.get(reverse('user:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/register.html')
        self.failUnless(response.context['form', UserRegistrationForm])

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('user:register'), data={
            'email': 'amir@gmail.com',
            'full_name': 'amir',
            'password': 'com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_user_register_POST_invalid(self):
        resp = self.client.post(reverse('user:register'), data={
            'email': 'amir_gmail.com',
            'full_name': 'amir',
            'password': 'com',
        })
        self.assertEqual(resp.status_code, 200)
        self.failIf(resp.context['form'].is_valid())
        self.assertFormError(resp, 'form', field='email', errors=_(['یک ایمیل معتبر را وارد کنید  ']))
