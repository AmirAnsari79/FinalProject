from django.urls import path
from . import views

app_name = 'basket'
urlpatterns = [

    path('det/', views.detail, name='basket_detail'),
    path('add/<int:ProductId>/', views.AddProduct, name='AddProduct')
]
