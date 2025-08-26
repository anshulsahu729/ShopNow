from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser

from .forms import SignupForm, LoginForm


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('accounts:login')  # ✅ Use namespace
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    error = None

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                login(request, user, backend='accounts.backends.SHAAuthBackend')
                return redirect('cart:cart_detail')  # ✅ Use namespace
            else:
                error = "Invalid password"
        except CustomUser.DoesNotExist:
            error = "User not found"

    return render(request, 'accounts/login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # ✅ Use namespace

