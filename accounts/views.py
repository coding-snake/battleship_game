from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
# Create your views here.

def accounts_view(request):
    context = {}
    return render(request, 'accounts.html', context)

def register(request):
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