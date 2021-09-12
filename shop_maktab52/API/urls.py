from django.urls import path, include

from API.views import ProductViews, ProductOnlyViews

app_name = 'API'
urlpatterns = [
    path('products/', ProductOnlyViews.as_view(), name='ProductListViews'),
    path('product/<int:pk>', ProductViews.as_view(), name='ProductViews'),

]
