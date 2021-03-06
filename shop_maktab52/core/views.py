from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView

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


#
#
# @login_required
# def profile(request):
#     # profile = Profiles.objects.get(user=request.user) if Profiles.objects.filter(user=request.user) else \
#     #     Profiles.objects.create(user=request.user)
#     pass
#     # order_item = OrderItem.objects.filter(order__user=request.user.id)
#     # return render(request, 'profile/profile.html', {'profile': profile, 'order_item': order_item})


class Profile(LoginRequiredMixin, ListView):
    template_name = 'profile/profile.html'

    queryset = Profiles.objects.all()

    def get_context_data(self, **kwargs):
        kwargs['order_item'] = OrderItem.objects.filter(order__user=self.request.user.id)
        kwargs['profile'] = Profiles.objects.get(user=self.request.user) if Profiles.objects.filter(
            user=self.request.user) else \
            Profiles.objects.create(user=self.request.user)
        return super().get_context_data(**kwargs)


@login_required
def ProfileEdit(request):
    _instance = Profiles.objects.get(user=request.user) if Profiles.objects.filter(user=request.user) else \
        Profiles.objects.create(user=request.user)
    if request.method == 'POST':
        # print(Profiles.objects.get(user=request.user))

        profile_form = ProfileEditForm(request.POST, instance=_instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('core:profile')
    else:
        profile_form = ProfileEditForm(instance=_instance)
    return render(request, 'profile/profile_edit.html', {'profile_form': profile_form})
