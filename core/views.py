from django.shortcuts import render,redirect
from store.models import Category, Product, Order
from django.contrib import messages
from newsletter.models import Subscriber
from django.shortcuts import render, get_object_or_404
from cart.models import Cart



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # You can save this to a model or send email
        # For now, we'll just display a success message
        messages.success(request, "Thank you for contacting us! We will get back to you soon.")

    return render(request, 'core/contact.html', {'title': 'Contact Us'})





def home(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "🎉 Thank you for subscribing!")
            else:
                messages.info(request, "You are already subscribed.")
        else:
            messages.error(request, "Please enter a valid email.")
        return redirect('core:home')  # Replace 'home' with your homepage URL name
    categories = Category.objects.all()[:4]
    category_products = {}
    for category in categories:
        category_products[category] = Product.objects.filter(
            category=category, active=True
        )[:4]
    products = Product.objects.filter(active=True)[:8]
    
    context = {
        'category_products': category_products,
        'products': products,
    }

    return render(request, 'core/home.html', context)


def product_list(request):
    products = Product.objects.filter(active=True)
    return render(request, 'core/product.html', {'products': products})



def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, active=True)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'core/category_products.html', context)
