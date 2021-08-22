from django.db import models
from django.conf import settings
from product.models import Product
from django.utils.translation import gettext as _
from core.models import BaseModel


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name=_('کاربر')
    )
    payment = models.BooleanField(default=False, verbose_name=_('برداخت'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('ساخته شده در '))
    update = models.DateTimeField(auto_now=True, verbose_name=_('تنظیم شده در '))

    class Meta:
        ordering = ('created', 'update')
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش'

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    def get_total_price(self):
        return sum(item.get_price() for item in self.items.all())


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
        return self.price * self.Number
