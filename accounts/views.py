from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

User = get_user_model()  # ✅ safely respects AUTH_USER_MODEL


def user_list(request):
    """ List all users (admin/demo purpose). """
    users = User.objects.all()
    return render(request, "accounts/user_list.html", {"users": users})


def signup_view(request):
    """ Handle user signup. """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # ✅ Always hash password properly
            raw_password = form.cleaned_data["password"]
            user.set_password(raw_password)
            user.save()
            return redirect("accounts:login")  # after signup go to login
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    """ Handle user login. """
    form = LoginForm(request.POST or None)
    error = None

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        # ✅ authenticate() calls custom backends from AUTHENTICATION_BACKENDS
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard:dashboard")
        else:
            error = "Invalid email or password"

    return render(request, "accounts/login.html", {"form": form, "error": error})


@login_required
def logout_view(request):
    """ Handle user logout. """
    logout(request)
    return redirect("accounts:login")
