SESSION_ID = 'cart'


class Basket:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(SESSION_ID)
        if not cart:
            cart = self.session[SESSION_ID] = {}
        self.cart = cart

