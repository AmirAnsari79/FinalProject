from django.urls import path
from . import views

app_name = 'basket'
urlpatterns = [

    path('det/', views.detail, name='basket_detail'),
    path('add/<int:product_id>/', views.AddProduct, name='AddProduct'),
    path('remove/<int:product_id>/', views.Basket_remove, name='Basket_remove'),
]
