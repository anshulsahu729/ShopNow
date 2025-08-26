from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class SHAAuthBackend(BaseBackend):
    """
    Custom backend that authenticates using email + password.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get("email", username)  # allow email as username
        if email is None or password is None:
            return None

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
