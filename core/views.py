from django.shortcuts import render
from store.models import Category, Product, Order

from django.contrib import messages

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

# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'core/home.html', context)