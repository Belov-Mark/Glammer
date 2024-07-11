from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(label='E-Mail')

    class Meta:
        model = User
        fields = ['email', 'password']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-Mail')

    class Meta:
        model = User
        fields = ['email',
                  'password1',
                  'password2',
                  'name',
                  'surname',
                  'number',
                  'date',
                  'sex']
