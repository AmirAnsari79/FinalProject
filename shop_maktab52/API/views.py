from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import *
from .permissions import *
from API.serializers import ProductSerializer
from product.models import Product
from rest_framework import permissions


class ProductViews(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAdminOrAuthReadOnly,)
    permission_classes = (permissions.IsAuthenticated, IsAdminEditable)


class ProductOnlyViews(ListCreateAPIView):
    queryset = Product.objects.filter(Available=True)
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminEditable)
