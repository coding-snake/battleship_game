from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class LoginUserForm(forms.Form):
    username_or_email = forms.CharField(label="Nazwa użytkownika albo email", max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    