# dashboard/urls.py
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("admin_r/", views.DashboardRouterView.as_view(), name="dashboard-router"),
    path("admin_h/", views.AdminDashboardView.as_view(), name="admin-home"),
    path("user/", views.UserDashboardView.as_view(), name="user-home"),
]
