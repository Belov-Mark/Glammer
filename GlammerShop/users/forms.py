from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['sex', 'name', 'surname', 'email', 'number', 'date', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-Mail', max_length=254)

from django import forms

class VerificationForm(forms.Form):
    verification_code = forms.CharField(label='Код подтверждения', max_length=8, min_length=8)
