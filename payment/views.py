from django.shortcuts import render, redirect
from .forms import CustomerOrderForm
from .models import CustomerOrder

def checkout_form_view(request):
    if request.method == 'POST':
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Redirect to “fake payment success” page
            return redirect('payment:payment_success', order_id=order.id)
    else:
        form = CustomerOrderForm()
    return render(request, 'payment/checkout_form.html', {'form': form})

def payment_success_view(request, order_id):
    order = CustomerOrder.objects.get(id=order_id)
    return render(request, 'payment/payment_success.html', {'order': order})
