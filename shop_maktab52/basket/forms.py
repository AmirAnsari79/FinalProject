from django import forms


class AddForm(forms.Form):
    Number = forms.IntegerField(min_value=1, max_value=10)
