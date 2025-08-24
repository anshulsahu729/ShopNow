# dashboard/mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin

class AdminManagerOnly(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.role in ["ADMIN", "MANAGER"]
        )
