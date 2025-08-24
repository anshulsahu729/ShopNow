# dashboard/views.py
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from accounts.models import Roles  # your custom Roles enum

class DashboardRouterView(LoginRequiredMixin, TemplateView):
    login_url = "/accounts/login/"   # where to redirect if not logged in

    def dispatch(self, request, *args, **kwargs):
        # ✅ At this point, user is guaranteed authenticated
        role = request.user.role  

        if role == Roles.ADMIN:
            return redirect("dashboard:admin-home")
        if role == Roles.MANAGER:
            return redirect("dashboard:manager-home")
        return redirect("dashboard:user-home")
    
    
class AdminDashboardView(LoginRequiredMixin, View):
    template_name = "dashboard/admin_dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  
    
class UserDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "dashboard/user_dashboard.html")
      
