from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout_view, name='checkout_view'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]
