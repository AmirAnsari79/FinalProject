from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from basket.forms import AddForm
from basket.sessions import Basket
from core.forms import SearchFormProduct, ProfileEditForm
from order.models import Order, OrderItem
from product.models import Product, Category
from user.views import User
from user.models import User, Profiles


def Home_Land(request, slug=None):
    products = Product.objects.filter(Available=True)
    categories = Category.objects.filter(IsSubCategory=False)
    # product_instance = Product()
    # check = product_instance.is_empty()
    search_form = SearchFormProduct(request.GET)
    if slug:
        category = get_object_or_404(Category, Slug=slug)
        products = products.filter(Category=category)
    if search_form.is_valid():
        products = products.filter(Name__contains=search_form.cleaned_data['product_name'])

    min_price, max_price = search_form.get_level_price()
    if min_price is not None:
        products = products.filter(Price__gte=min_price)
    if max_price is not None:
        products = products.filter(Price__lt=max_price)
    else:
        pass
    content = {
        'products': products,
        'categories': categories,
        'search_form': search_form
        # 'check_store': check
    }
    # print(check)
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
    profile = Profiles.objects.get(user=request.user.id)
    order_item = OrderItem.objects.filter(order__user=request.user.id)
    return render(request, 'profile/profile.html', {'profile': profile, 'order_item': order_item})


@login_required
def ProfileEdit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('core:profile')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'profile/profile_edit.html', {'profile_form': profile_form})
