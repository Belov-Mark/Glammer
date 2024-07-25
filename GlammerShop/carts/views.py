# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

from products.models import Product
from .models import Cart, CartItem
from .forms import AddToCartForm
import uuid

class CartView(View):
    def get(self, request):
        cart = self.get_cart(request)
        return render(request, 'carts/cart.html', {'cart': cart})

    def post(self, request):
        action = request.POST.get('action')
        if action == 'add':
            form = AddToCartForm(request.POST)
            if form.is_valid():
                product = form.cleaned_data['product']
                quantity = form.cleaned_data['quantity']
                cart = self.get_cart(request)
                cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
                if not created:
                    cart_item.quantity += quantity
                    cart_item.save()
                else:
                    cart_item.quantity = quantity
                    cart_item.save()
                return redirect('carts:cart')
        elif action == 'remove':
            product_id = request.POST.get('product_id')
            cart = self.get_cart(request)
            cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
            cart_item.delete()
            return redirect('carts:cart')

    def get_cart(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart_cookie = request.COOKIES.get('cart_cookie')
            if cart_cookie:
                cart, created = Cart.objects.get_or_create(cart_cookie=cart_cookie)
            else:
                cart_cookie = str(uuid.uuid4())
                cart, created = Cart.objects.get_or_create(cart_cookie=cart_cookie)
                response = redirect('carts:cart')
                response.set_cookie('cart_cookie', cart_cookie)
                response.save()
        return cart
    
class AddToCartView(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)
        cart = self.get_cart(request)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Перенаправление на предыдущую страницу

    def get_cart(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart_cookie = request.COOKIES.get('cart_cookie')
            if cart_cookie:
                cart, created = Cart.objects.get_or_create(cart_cookie=cart_cookie)
            else:
                cart_cookie = str(uuid.uuid4())
                cart, created = Cart.objects.get_or_create(cart_cookie=cart_cookie)
                response = redirect('carts:cart')
                response.set_cookie('cart_cookie', cart_cookie)
                response.save()
        return cart
