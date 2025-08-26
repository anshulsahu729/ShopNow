from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import hashlib
import datetime 
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email is required')
        if not name:
            raise ValueError('Name is required')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email=email, name=name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=255 ,default="Anonymous")  # ✅ Added name field
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # ✅ Require name  for creates

    objects = UserManager()

    def set_password(self, raw_password):
        self.password = hashlib.sha256(raw_password.encode()).hexdigest()

    def check_password(self, raw_password):
        return self.password == hashlib.sha256(raw_password.encode()).hexdigest()

    def __str__(self):
        return self.name or self.email  # Show name if available

    @property
    def is_staff(self):
        return self.is_admin
class CustomUser(AbstractUser):
    # Extra fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Avoid reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # change from default
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # change from default
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username