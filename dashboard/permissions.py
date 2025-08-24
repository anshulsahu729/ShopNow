# dashboard/permissions.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from accounts.models import Roles


class RoleRequiredMixin(LoginRequiredMixin):
    """Base Mixin to restrict dashboard views by role(s)."""
    allowed_roles: tuple[str, ...] = ()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.allowed_roles and request.user.role not in self.allowed_roles:
            raise PermissionDenied("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)


class AdminOnly(RoleRequiredMixin):
    allowed_roles = (Roles.ADMIN,)


class AdminManagerOnly(RoleRequiredMixin):
    allowed_roles = (Roles.ADMIN, Roles.MANAGER)


class AnyAuthenticated(RoleRequiredMixin):
    """Any logged-in user (admin, manager, or customer)."""
    allowed_roles = (Roles.ADMIN, Roles.MANAGER, Roles.CUSTOMER)
