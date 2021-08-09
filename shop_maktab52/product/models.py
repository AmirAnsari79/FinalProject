from django.db import models
from django.urls import reverse

from core.models import BaseModel


class Product(BaseModel):
    Category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='Product'
    )
    Name = models.CharField(max_length=255)
    Slug = models.SlugField(max_length=100, unique=True)
    Images = models.ImageField(upload_to='Product/%y/%m/%d/%h/')
    description = models.TextField()
    Price = models.DecimalField(max_digits=12, decimal_places=3)
    Available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('core:product_details', args=[self.Slug])

    def __str__(self):
        return self.Name


class Category(BaseModel):
    Name = models.CharField(max_length=150)
    Slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Name
