# dashboard/views.py
from django.shortcuts import redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from store.models import Category, Product, Order


 # ✅ Only staff/admins can access
def admin_dashboard(request):
    category_count = Category.objects.count()
    product_count = Product.objects.count()
    order_count = Order.objects.count()

    # Get recent 5 orders
    recent_orders = Order.objects.order_by('-created_at')[:5]

    context = {
        'category_count': category_count,
        'product_count': product_count,
        'order_count': order_count,
        'recent_orders': recent_orders,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

