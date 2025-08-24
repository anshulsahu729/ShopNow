# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    # registration
    path("register/", views.register_view, name="register"),

    # login/logout using Django’s built-in views
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login",
    ),
    path("logout/", views.logout_view, name="logout"),

    # dashboard (role-based)
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
