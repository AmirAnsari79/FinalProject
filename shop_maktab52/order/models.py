# from django.db import models
# from django.conf import settings
# from product.models import Product
#
# from core.models import BaseModel
#
#
# class OrderItem(BaseModel):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name='product_OrderItem'
#     )
#
#     order = models.ForeignKey(
#         'Order', on_delete=models.CASCADE, related_name='item'
#     )
#     price = models.DecimalField(max_digits=12,decimal_places=2)
#     Number = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f'order_id :{self.id} '
#
#     def get_price(self):
#         return self.price * self.Number
#
#
# class Order(BaseModel):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order'
#     )
#     payment = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return self.user
#
#     def get_price(self):
#         pass
