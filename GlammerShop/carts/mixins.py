from .models import Cart


class ReceivingCartMixin:
    def get_cart(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart_cookie = request.COOKIES.get('cart_cookie')
            if not cart_cookie:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
            else:
                cart = Cart.objects.get(id=cart_cookie)
        return cart

