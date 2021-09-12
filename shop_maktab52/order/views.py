from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _
from basket.sessions import Basket
from .forms import CouponForm
from order.models import Order, OrderItem, Coupon


@login_required
def payment(request, order_id):
    order_pay = Order.objects.get(id=order_id)
    order_pay.payment = True
    order_pay.save()
    messages.success(request, 'success payment', 'success')
    return redirect('core:home')


@login_required
def detail(request, order_id):
    form = CouponForm()
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order.html', {'order': order, 'form': form})


@login_required
def order_creat(request):
    basket = Basket(request)
    order = Order.objects.create(user=request.user, )
    for item in basket:
        OrderItem.objects.create(
            order=order, product=item['product'], price=item['price'], Number=item['Number']
        )
    basket.clear()
    return redirect('order:detail', order.id)


@login_required
@require_POST
def coupon_apply(request,order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
        except Coupon.DoesNotExist:
            messages.error(request, _('این کد در دسترس نیست '))
            return redirect('order:detail', order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount
        order.save()
    return redirect('order:detail', order_id)
