from django.apps import AppConfig
from django.utils.translation import gettext as _


class BasketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
