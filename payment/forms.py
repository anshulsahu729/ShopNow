from django import forms
from .models import CustomerOrder

class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['name', 'email', 'phone', 'bank_account', 'product_name', 'amount', 'payment_method']
        widgets = {
            'payment_method': forms.RadioSelect
        }
