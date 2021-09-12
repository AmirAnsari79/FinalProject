from django.urls import path, include

from API.views import ProductViews, ProductOnlyViews

app_name = 'API'
urlpatterns = [
    path('product/<int:pk>', ProductViews.as_view(), name='ProductViews'),
    path('product', ProductOnlyViews.as_view(), name='ProductViews'),

]
