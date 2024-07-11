from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['sex', 'name', 'surname', 'email', 'number', 'date', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-Mail', max_length=254)

