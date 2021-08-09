from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('Home/', views.Home_Land, name='home'),
    path('<slug:slug>/', views.Product_Details, name='product_details'),
    path('categories/<slug:slug>', views.Home_Land, name="categories_sort")
]
