from decimal import Decimal

from django.db import models
from django.conf import settings
from product.models import Product
from django.utils.translation import gettext as _
from core.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name=_('کاربر')
    )
    payment = models.BooleanField(default=False, verbose_name=_('برداخت'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('ساخته شده در '))
    update = models.DateTimeField(auto_now=True, verbose_name=_('تنظیم شده در '))
    discount = models.IntegerField(blank=True, null=True, default=None, verbose_name=_(' تخفیف'))

    class Meta:
        ordering = ('created', 'update')
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش'

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    @property
    def get_total_price(self):
        total = sum(item.get_price() for item in self.items.all())
        if self.discount:
            discount_price = Decimal((self.discount / 100) * total)
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_OrderItem', verbose_name=_('محصول')
    )

    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name='items', verbose_name=_('سفارش')
    )
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('قیمت'))
    Number = models.PositiveIntegerField(default=1, verbose_name=_('تعداد'))

    class Meta:
        verbose_name = 'آیتم سفارش'
        verbose_name_plural = 'آیتم سفارش'

    def __str__(self):
        return str(self.id)

    def get_price(self):
        return int(self.price * self.Number)


class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name=_('نام کد تخفیف'))
    valid_from = models.DateTimeField(verbose_name=_('از '))
    valid_to = models.DateTimeField(verbose_name=_('تا'))
    discount = models.IntegerField(verbose_name=_(' درصد تخفیف'),
                                   validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=False, verbose_name=_('فعال بودن'))

    class Meta:
        verbose_name = _('کد تخفیف')
        verbose_name_plural = _('کد تخفیف')

    def __str__(self):
        return self.code
