from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm as BaseUserChangeForm
from django.forms import widgets

from citys.models import City
from .models import User


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not email or not password:
            raise forms.ValidationError('Email и пароль должны быть заполнены')

        return cleaned_data




class SignInForm(UserCreationForm):
    sex = forms.ChoiceField(choices=[('M', 'М'), ('F', 'Ж')], widget=forms.RadioSelect(attrs={'class': 'sex'}), label='Пол')
    name = forms.CharField(max_length=50, label='Имя')
    surname = forms.CharField(max_length=50, label='Фамилия')
    email = forms.EmailField(label='Email')
    number = forms.CharField(max_length=20, widget=widgets.TextInput(attrs={'type': 'tel'}), label='Контактный номер')
    date = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}), label='Дата рождения')
    city = forms.ModelChoiceField(queryset=City.objects.all(), initial=3, widget=widgets.Select(attrs={'class': 'city'}), label='Город')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['sex', 'name', 'surname', 'email', 'number', 'date', 'city', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Проверка совпадения паролей
        if password1 != password2:
            self.add_error('password2', 'Пароли не совпадают')

        return cleaned_data

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ['sex', 'name', 'surname', 'email', 'number', 'date', 'city', 'password', 'is_active', 'is_staff', 'is_superuser']

class VerificationCodeForm(forms.ModelForm):
    """
    Форма для ввода кода подтверждения.
    """
    code = forms.CharField(max_length=8, min_length=8, label='Код подтверждения')

    def clean_code(self):
        """
        Проверка кода подтверждения.
        """
        code = self.cleaned_data.get('code')
        if len(code) != 8:
            raise forms.ValidationError('Код должен состоять из 8 цифр.')
        return code

class ResendCodeForm(forms.ModelForm):
    """
    Форма для повторной отправки кода подтверждения.
    """
    # Поле не требуется, так как повторная отправка кода выполняется для текущего пользователя.
    class Meta:
        model = User
        fields = []
