from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.models import Cart, CartItem


@login_required(login_url='accounts:login')  # ✅ force login
def checkout_view(request):
    # Get the cart for the logged-in user
    cart = Cart.objects.filter(user=request.user).first()

    # If no cart or empty cart
    if not cart or not cart.items.exists():
        return redirect('cart:cart_view')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = sum(
                item.product.price * item.quantity
                for item in cart.items.all()
            )
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
        form = CheckoutForm(initial={
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email
        })

    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'form': form
    })


@login_required(login_url='accounts:login')
def thank_you_view(request):
    return render(request, 'checkout/thank_you.html')
