from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = "__all__"
        exclude = ('Store',)

