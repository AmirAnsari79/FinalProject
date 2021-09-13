from django import forms
from django.utils.translation import gettext as _
from user.models import Profiles


class SearchFormProduct(forms.Form):
    product_name = forms.CharField(max_length=50, required=False, label=_('نام محصول'))
    any_price = '0'
    until_50 = '1'
    as_50_to_100 = '2'
    as_100_to_500 = '3'
    as_500_to_1 = '4'
    gatter_1 = '5'
    CHOICE = (
        (any_price, _('هر قیمتی')),
        (until_50, _('تا ۵۰ هزار تومان')),
        (as_50_to_100, _('از ۵۰ تا ۱۰۰ هزارتومان')),
        (as_100_to_500, _('از ۱۰۰ تا ۵۰۰هزارتومان')),
        (as_500_to_1, _('از ۵۰۰هزارتومان تا ۱ میلیون تومان')),
        (gatter_1, _('بیش از یک میلیون تومان')),
    )
    price = forms.ChoiceField(label=_('محدوده ی قیمت '), choices=CHOICE, required=False)

    def get_level_price(self):
        price = self.cleaned_data['price']
        if price == SearchFormProduct.until_50:
            return None, 50000
        elif price == SearchFormProduct.as_50_to_100:
            return 50000, 100000
        elif price == SearchFormProduct.as_100_to_500:
            return 100000, 500000
        elif price == SearchFormProduct.as_500_to_1:
            return 500000, 1000000
        elif price == SearchFormProduct.gatter_1:
            return 1000000, None
        else:
            return None, None


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['Address', 'Mobile']
