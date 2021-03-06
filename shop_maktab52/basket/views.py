from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from .forms import AddForm
from .sessions import Basket
from django.contrib import messages
from django.views.decorators.http import require_POST
from user.models import User
from django.utils.translation import gettext as _


# Create your views here.
def detail(request):
    basket = Basket(request)
    context = {
        'basket': basket,

    }
    return render(request, 'basket/Basket_receipts.html', context)


@require_POST
def AddProduct(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        if product.CheckStore(number=cd['Number']):
            basket.add(product=product, Number=cd['Number'])
        else:
            messages.error(request, _('موجودی انبار کافی نیست'))
        # if
    return redirect('basket:basket_detail')


def Basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.Remove(product)
    return redirect('basket:basket_detail')
