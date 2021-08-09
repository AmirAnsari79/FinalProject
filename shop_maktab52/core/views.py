import content as content
from django.shortcuts import render, get_object_or_404
from product.models import Product, Category


def Home_Land(request, slug=None):
    products = Product.objects.filter(Available=True)
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, Slug=slug)
        products = products.filter(Category=category)
    content = {
        'products': products,
        'category': categories
    }
    return render(request, 'core/home.html', content)


def Product_Details(request, slug):
    product = get_object_or_404(Product, Slug=slug)
    content = {
        'product': product,
    }
    return render(request, 'core/detailproduct.html', content)
