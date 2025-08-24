# dashboard/views.py
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from store.models import Product  # adjust app/model if different

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "dashboard/products/product_confirm_delete.html"
    success_url = reverse_lazy("dashboard:product-list")
