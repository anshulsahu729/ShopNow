from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('checkout/', views.checkout_form_view, name='checkout_form'),
    path('success/<int:order_id>/', views.payment_success_view, name='payment_success'),
]
