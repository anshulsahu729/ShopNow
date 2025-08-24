# accounts/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import Roles


def register_view(request):
    """Customer (default) registration form."""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            messages.success(request, "Account created successfully!")
            return redirect("accounts:dashboard")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def dashboard_view(request):
    """Role-based dashboard routing."""
    user = request.user
    context = {"user": user}

    if user.role == Roles.CUSTOMER:
        template = "accounts/dashboard_customer.html"
    elif user.role == Roles.SELLER:
        template = "accounts/dashboard_seller.html"
    elif user.role == Roles.MANAGER:
        template = "accounts/dashboard_manager.html"
    elif user.role in [Roles.ADMIN, Roles.STAFF]:
        template = "accounts/dashboard_admin.html"
    else:
        template = "accounts/dashboard_generic.html"

    return render(request, template, context)


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect(reverse("accounts:login"))

