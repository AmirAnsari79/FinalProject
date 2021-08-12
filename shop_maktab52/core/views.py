from django.shortcuts import render, get_object_or_404
from product.models import Product, Category
from basket.forms import AddForm


def Home_Land(request, slug=None):
    products = Product.objects.filter(Available=True)
    categories = Category.objects.filter(IsSubCategory=False)
    if slug:
        category = get_object_or_404(Category, Slug=slug)
        products = products.filter(Category=category)
    content = {
        'products': products,
        'categories': categories
    }
    return render(request, 'base.html', content)


def Product_Details(request, slug):
    product = get_object_or_404(Product, Slug=slug)
    form_add = AddForm()
    content = {
        'product': product,
        'form': form_add
    }
    return render(request, 'core/detailproduct.html', content)
