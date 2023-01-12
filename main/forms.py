from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    telegram = forms.CharField(max_length = 50 , required = True)
    phone = forms.CharField(max_length = 11 , required = True)

    class Meta:
        model = User
        fields = ["username" , "email" , "phone" , "telegram" , "password1" , 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100 , required = True)
    password = forms.CharField(max_length = 100 , required = True , widget = forms.PasswordInput)