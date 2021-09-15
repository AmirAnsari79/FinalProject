from django import forms
from django.utils.translation import gettext as _


class AddForm(forms.Form):
    Number = forms.IntegerField(min_value=1, max_value=10, label=_('تعداد '))
