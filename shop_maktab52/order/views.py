from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from basket.sessions import Basket

from order.models import Order, OrderItem


@login_required
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order.html', {'order': order})


@login_required
def order_creat(request):
    basket = Basket(request)
    order = Order.objects.create(user=request.user, )
    for item in basket:
        OrderItem.objects.create(
            order=order, product=item['product'], price=item['price'], Number=item['Number']
        )
        # basket.clear()
    return redirect('order:detail', order.id)


@login_required
def payment(request, order_id):
    order_pay = Order.objects.get(id=order_id)
    order_pay.payment = True
    order_pay.save()
    messages.success(request, 'success payment', 'success')
    return redirect('core:home')
