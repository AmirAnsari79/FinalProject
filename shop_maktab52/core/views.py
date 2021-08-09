import content as content
from django.shortcuts import render, get_object_or_404
from product.models import Product


def Home_Land(request):
    products = Product.objects.filter(Available=True)
    content = {
        'products': products,
    }
    return render(request, 'core/home.html', content)


def Product_Details(request, slug):
    product = get_object_or_404(Product, Slug=slug)
    content = {
        'product': product,
    }
    return render(request, 'core/detailproduct.html', content)
