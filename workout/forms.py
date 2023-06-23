from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import admin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'height', 'weight', 'password1']

class LoginForm(AuthenticationForm):
    pass