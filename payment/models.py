from django.db import models
from django.utils import timezone
from datetime import timedelta

class CustomerOrder(models.Model):
    PAYMENT_CHOICES = [
        ('UPI', 'UPI/Online Payment'),
        ('COD', 'Cash on Delivery'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    product_name = models.CharField(max_length=200)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    order_date = models.DateTimeField(default=timezone.now)
    
    @property
    def delivery_date(self):
        return self.order_date + timedelta(days=3)

    def __str__(self):
        return f"{self.name} - {self.product_name}"
