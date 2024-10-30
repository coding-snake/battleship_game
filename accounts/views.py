from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm
from .auth_back import auth_with_email_or_username

# Create your views here.

def accounts_view(request):
    context = {}
    return render(request, 'accounts.html', context)

def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rejestracja przebiegła z sukcesem!")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    context = {'form' : form}
    return render(request, 'register.html', context)

def login_view(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username_or_email = request.POST.get('username_or_email')
            password = request.POST.get('password')

            authenticator = auth_with_email_or_username()
            user = authenticator.authenticate(request=request, username_or_email=username_or_email, password=password)

            if user is not None:
                login(request, user, backend='accounts.auth_back.auth_with_email_or_username')
                return redirect('home')
            else:
                messages.error(request, "Użytkownik nie znaleziony")
        
    context = {'form' : form}
    return render(request, 'login.html', context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, 'logout.html')