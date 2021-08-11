from django.urls import path
from . import views

app_name = 'basket'
urlpatterns = [

    path('det/', views.detail, name='detail'),
    path('basket/add/<int:ProductId>/', views.AddProduct, name='AddProduct')
]
