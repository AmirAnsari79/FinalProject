from django.db import models
from django.conf import settings
from product.models import Product

from core.models import BaseModel


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders'
    )
    payment = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created', 'update')

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    def get_total_price(self):
        return sum(item.get_price() for item in self.items.all())


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_OrderItem'
    )

    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name='items'
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    Number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_price(self):
        return self.price * self.Number
