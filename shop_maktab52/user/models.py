from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager
from django.utils.translation import gettext as _


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name=_('ایمیل'))
    full_name = models.CharField(max_length=100, verbose_name=_('نام '))
    is_admin = models.BooleanField(default=False, verbose_name=_('ادمین بودن '))
    is_active = models.BooleanField(default=True, verbose_name=_('فعال بودن'))
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربر')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


# class Profile(models.Model):
#     Address = models.TextField(verbose_name=_(''))
#     Mobile = models.DecimalField(verbose_name=_(''), max_digits=11, decimal_places=0)
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name='Profile', verbose_name=_('کاربر')
#     )
#
#     class Meta:
#         verbose_name = _('حساب کاربری')
#         verbose_name_plural = _('حساب کاربری')
