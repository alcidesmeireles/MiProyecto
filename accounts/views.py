from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login

# Signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Login
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

# Logout
class UserLogoutView(LogoutView):
    next_page = 'login'
    http_method_names = ['get', 'post']

# Profile view
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# Profile edit
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})

# Change password
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('profile')