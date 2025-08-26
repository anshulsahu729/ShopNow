# dashboard/urls.py
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("manager/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/", views.user_dashboard, name="user_dashboard"),
]
