from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from core.models import BaseModel


class Product(models.Model):
    Category = models.ManyToManyField(
        'Category', related_name='categories', verbose_name=_('دسته بندی')
    )
    Name = models.CharField(max_length=255, verbose_name=_('نام محصول'))
    Slug = models.SlugField(max_length=100, unique=True)
    Images = models.ImageField(upload_to='Product/%y/%m/%d/%h/', verbose_name=_('عکس'))
    description = models.TextField(verbose_name=_('اطلاعات'))
    Price = models.PositiveIntegerField(verbose_name=_('قیمت'))
    Available = models.BooleanField(default=True, verbose_name=_('دسترسی'))
    Store = models.PositiveIntegerField(verbose_name=_('تعداد محصول'))
    created_at = models.DateTimeField(auto_now_add=True, )

    class Meta:
        verbose_name = _('محصول')
        verbose_name_plural = _('محصول')

    def get_absolute_url(self):
        return reverse('core:product_details', args=[self.Slug])

    def __str__(self):
        return self.Name

    def get_price_display(self):
        return f'{self.Price}  تومان '

    def is_empty(self):
        return self.Store == 0

    def CheckStore(self, number):
        if self.Store < number:
            self.Store -= number
            self.save()
            return True
        else:
            self.Store -= number
            self.save()
            return True


class Category(BaseModel):
    Name = models.CharField(max_length=150, verbose_name=_(''))
    Slug = models.SlugField(max_length=100, unique=True, verbose_name=_(''))
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name="SubCategory", null=True, blank=True, verbose_name=_('')
    )
    IsSubCategory = models.BooleanField(default=False, verbose_name=_('زیر دسته بندی'))
    """
    if default=True ==> category is child
    else default=False ==> category is self (koli)
    """

    class Meta:
        ordering = ('Name',)
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی')

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('core:categories_sort', args=[self.Slug])
