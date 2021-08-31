from django import forms
from django.utils.translation import gettext as _


class CouponForm(forms.Form):
    code = forms.CharField(label='')
