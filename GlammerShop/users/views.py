from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import HttpRequest, HttpResponse
from datetime import datetime, date

from .forms import UserLoginForm, UserRegisterForm, VerificationForm
from .utils import send_verification_code


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    
    def get_success_url(self) -> str:
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        messages.success(self.request, 'Вы успешно вошли!')
        return reverse_lazy('main:main')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context


class UserSigninView(CreateView):
    template_name = 'users/signin.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form) -> HttpResponse:
        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        code, code_validity = send_verification_code(email, name)
        self.request.session['code'] = code
        self.request.session['code_validity'] = code_validity.isoformat()  # Сохранение даты в строковом формате
        user_data = form.cleaned_data
        for key, value in user_data.items():
            if isinstance(value, date):
                user_data[key] = value.isoformat()  # Преобразование даты в строку
        self.request.session['user_data'] = user_data
        return super().form_valid(form)


class VerifyCodeView(View):
    template_name = 'users/verification.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = VerificationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = VerificationForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['code']
            stored_code = request.session.get('code')
            code_validity_str = request.session.get('code_validity')
            code_validity = datetime.fromisoformat(code_validity_str) if code_validity_str else None

            if entered_code == stored_code and now() < code_validity:
                user_data = request.session.get('user_data')
                if user_data:
                    for key, value in user_data.items():
                        if isinstance(value, str) and len(value) == 10:  # Пример простого условия для даты
                            try:
                                user_data[key] = date.fromisoformat(value)  # Преобразование строки обратно в дату
                            except ValueError:
                                messages.error(request, f'Ошибка преобразования значения для {key}.')
                                return redirect('users:signin')
                    user_form = UserRegisterForm(user_data)
                    if user_form.is_valid():
                        user = user_form.save()
                        login(request, user)
                        messages.success(request, 'Регистрация прошла успешно!')
                        del request.session['code']
                        del request.session['code_validity']
                        del request.session['user_data']
                        return redirect('main:main')
                    else:
                        messages.error(request, 'Ошибка валидации формы регистрации.')
                        return redirect('users:signin')
                else:
                    messages.error(request, 'Данные пользователя не найдены в сессии.')
                    return redirect('users:signin')
            else:
                if entered_code != stored_code:
                    messages.error(request, 'Неверный код подтверждения. Попробуйте снова.')
                elif now() >= code_validity:
                    messages.error(request, 'Срок действия кода подтверждения истек. Запросите новый код.')
                return redirect('users:verification')
        else:
            messages.error(request, 'Ошибка валидации формы верификации. Попробуйте снова.')
            return redirect('users:verification')


def recovery(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'users/recovery.html', context)


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'users/profile.html', context)


@login_required
def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('main:index')
