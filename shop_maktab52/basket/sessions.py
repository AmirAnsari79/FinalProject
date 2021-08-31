from decimal import Decimal
from unicodedata import decimal

from product.models import Product

SESSION_ID = 'cart'


class Basket:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(SESSION_ID)
        if not cart:
            cart = self.session[SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        Productid = self.cart.keys()
        products = Product.objects.filter(id__in=Productid)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for _ in cart.values():
            _['total_price'] = Decimal(_['price']) * _['Number']
            yield _

    def Remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session_modification()

    def add(self, product, Number):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'Number': 0, 'price': str(product.Price)}
        self.cart[product_id]['Number'] += Number
        self.session_modification()

    def session_modification(self):
        self.session.modified = True

    def total_price(self):
        return sum(Decimal(_['price']) * _['Number'] for _ in self.cart.values())

    def clear(self):
        del self.session[SESSION_ID]
        self.session_modification()
