from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('create/', views.order_creat, name='create'),
    path('pay/<int:order_id>/', views.payment, name='payment'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('apply/<int:order_id>', views.coupon_apply, name='coupon_apply')
]
