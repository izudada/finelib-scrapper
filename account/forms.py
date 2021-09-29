from django import forms
from django.contrib.auth.forms import UserCreationForm
from  .models import User

from account.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField( max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)