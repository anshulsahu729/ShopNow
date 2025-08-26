from django.db import models
from django.utils.text import slugify
from django.conf import settings   # ✅ Use this instead of get_user_model()


# -------------------- CATEGORY --------------------
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------------------- PRODUCT --------------------
STATUS_CHOICES = [
    ("in_stock", "In Stock"),
    ("out_of_stock", "Out of Stock"),
    ("preorder", "Preorder"),
]

class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products"
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/")
    active = models.BooleanField(default=True)
    description = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# -------------------- ORDER --------------------
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # ✅ safest way for custom user models
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='orders'       # ✅ renamed to avoid future clashes
    )
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"


# -------------------- ORDER ITEM --------------------
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name="items"
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='order_items'   # ✅ simplified name
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} × {self.product.name if self.product else '[Deleted Product]'}"
