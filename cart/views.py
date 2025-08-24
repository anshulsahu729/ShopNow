from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from store.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart_view')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == "POST":
        cart.items.all().delete()  # Clear cart after checkout
        return redirect('thank_you')
    return render(request, 'cart/checkout.html', {'cart': cart})

@login_required
def thank_you(request):
    return render(request, 'cart/thank_you.html')
