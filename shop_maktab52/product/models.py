from django.db import models
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
