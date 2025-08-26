from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from store.models import Category, Product, Order



def admin_dashboard(request):
    category_count = Category.objects.count()
    product_count = Product.objects.count()
    order_count = Order.objects.count()

    recent_orders = Order.objects.order_by('-created_at')[:5]

    context = {
        'category_count': category_count,
        'product_count': product_count,
        'order_count': order_count,
        'recent_orders': recent_orders,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

  # redirect to your login URL name
def user_dashboard(request):
    
    return render(request, 'dashboard/dashboard.html')