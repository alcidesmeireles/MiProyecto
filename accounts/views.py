from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login
from django.contrib import messages  

# Signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect('profile')
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {"form": form})


# Login
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


# LOGOUT
class UserLogoutView(LogoutView):
    next_page = 'login'

    def dispatch(self, request, *args, **kwargs):
        # Forzar logout directo sin template
        if request.method == "GET":
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)






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
