from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from products.models import Product
from .models import CartItem
from .forms import AddToCartForm
from .mixins import ReceivingCartMixin

class CartView(ReceivingCartMixin, View):
    def get(self, request):
        cart = self.get_cart(request)
        print("Корзина:", cart)
        print("Элементы корзины:", list(cart.items.all()))
        response = render(request, 'carts/cart.html', {'cart': cart})
        
        # Устанавливаем куки, если это новый cart_cookie
        if not request.user.is_authenticated:
            cart_cookie = request.COOKIES.get('cart_cookie')
            if cart_cookie:
                response.set_cookie('cart_cookie', cart_cookie)
        
        return response

    def post(self, request):
        action = request.POST.get('action')
        cart = self.get_cart(request)

        if action == 'add':
            form = AddToCartForm(request.POST)
            if form.is_valid():
                product_id = form.cleaned_data['product_id']
                product = get_object_or_404(Product, id=product_id)
                cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
                if not created:
                    cart_item.quantity += 1
                else:
                    cart_item.quantity = 1
                cart_item.save()

        elif action == 'remove':
            product_id = request.POST.get('product_id')
            cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
            cart_item.delete()
        
        elif action == 'clear':
            cart.items.all().delete()

        return redirect(request.META.get('HTTP_REFERER', '/'))

class AddToCartView(ReceivingCartMixin, View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = 1
        product = get_object_or_404(Product, id=product_id)
        cart = self.get_cart(request)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
