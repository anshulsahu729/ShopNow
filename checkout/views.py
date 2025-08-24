from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from store.models import Order, OrderItem
from .forms import CheckoutForm
from django.utils import timezone

@login_required
def checkout_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or cart.items.count() == 0:
        return redirect('cart:cart_view')  # Redirect if cart empty

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price
            order.created_at = timezone.now()
            order.save()

            # Create OrderItems
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # Clear cart
            cart.items.all().delete()
            return redirect('checkout:thank_you')
    else:
        form = CheckoutForm(initial={'full_name': request.user.get_full_name(), 'email': request.user.email})

    return render(request, 'checkout/checkout.html', {'cart': cart, 'form': form})
    

@login_required
def thank_you_view(request):
    return render(request, 'checkout/thank_you.html')
