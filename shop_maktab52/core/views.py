from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from basket.forms import AddForm
from basket.sessions import Basket
from product.models import Product, Category
from user.views import User


def Home_Land(request, slug=None):
    products = Product.objects.filter(Available=True, created_at__lte=datetime.today())
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


@login_required
def Profile(request):
    get_object = User.objects.get(pk=request.user.id)
    return render(request, 'profile/profile.html', {'get': get_object})
