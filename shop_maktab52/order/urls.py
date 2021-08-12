from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('<int:order_id>/', views.payment, name='payment'),
    path('create/', views.order_creat, name='create'),
    path('<int:order_id>/', views.detail, name='detail'),

]
