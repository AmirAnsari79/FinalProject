from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from .forms import AddForm
from .sessions import Basket
from django.views.decorators.http import require_POST


# Create your views here.
def detail(request):
    basket = Basket(request)
    context = {
        'basket': basket,

    }
    return render(request, 'basket/detail.html',context)


@require_POST
def AddProduct(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product, Number=cd['Number'])
    return redirect('basket:basket_detail')