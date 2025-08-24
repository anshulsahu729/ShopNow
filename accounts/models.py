# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Roles(models.TextChoices):
    CUSTOMER = "customer", "Customer"
    SELLER   = "seller", "Seller"
    MANAGER  = "manager", "Manager"
    STAFF    = "staff", "Staff"     # separate from is_staff; use intentionally
    ADMIN    = "admin", "Admin"     # separate from is_superuser

class CustomUser(AbstractUser):
    # Keep username/email behavior from AbstractUser
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.CUSTOMER,
        help_text="Application-level role used for authorization & UI."
    )

    # convenience helpers
    @property
    def is_customer(self) -> bool:
        return self.role == Roles.CUSTOMER

    @property
    def is_seller(self) -> bool:
        return self.role == Roles.SELLER

    @property
    def is_manager(self) -> bool:
        return self.role == Roles.MANAGER

    def __str__(self) -> str:
        # show username + role for quick identification
        return f"{self.username} ({self.get_role_display()})"
