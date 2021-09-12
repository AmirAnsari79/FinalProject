from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', views.Home_Land, name='home'),
    path('categories/<slug:slug>', views.Home_Land, name="categories_sort"),
    path('<slug:slug>/', views.Product_Details, name='product_details'),
    path('profile', views.Profile, name='profile'),
    path('profile_edit', views.ProfileEdit, name='profile_edit'),

]
