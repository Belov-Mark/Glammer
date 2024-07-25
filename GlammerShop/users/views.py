from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.views.generic import CreateView
from .forms import SignInForm, LoginForm, VerificationCodeForm, ResendCodeForm
from .models import User
from .utils import generate_verification_code, is_code_valid

class SignInView(CreateView):
    """
    Представление для регистрации новых пользователей.
    """
    form_class = SignInForm
    template_name = 'users/signin.html'
    success_url = 'users/verification.html'  # URL для перенаправления после успешной регистрации

    def form_valid(self, form):
        """
        Метод, вызываемый при успешной отправке формы.
        """
        user = form.save(commit=False)  # Создает пользователя без сохранения
        user.is_active = False  # Пользователь не активен до подтверждения почты
        user.verification_code = generate_verification_code()  # Генерация кода подтверждения
        user.code_created_at = timezone.now()  # Устанавливаем время создания кода
        user.save()
        
        # Отправка email с кодом подтверждения
        send_mail(
            'Ваш код подтверждения',
            f'Ваш код подтверждения: {user.verification_code}',
            None,  # Используется адрес отправителя из настроек Django
            [user.email],  # Адрес получателя
            fail_silently=False,
        )
        messages.success(self.request, 'Регистрация успешна. Проверьте вашу почту для получения кода подтверждения.')
        return super().form_valid(form)

class LoginView(AuthLoginView):
    """
    Представление для входа пользователей.
    """
    form_class = LoginForm
    template_name = 'users/login.html'
    
    def get_success_url(self):
        """
        Метод, возвращающий URL для перенаправления после успешного входа.
        """
        return 'main:main'  # URL для перенаправления после входа

def logout_view(request):
    """
    Функция для выхода пользователя.
    """
    auth_logout(request)
    return redirect('users:login')

class VerifyCodeView(View):
    """
    Представление для ввода кода подтверждения после регистрации.
    """
    def get(self, request):
        form = VerificationCodeForm()
        return render(request, 'users:verification', {'form': form})

    def post(self, request):
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            user = User.objects.filter(email=request.user.email).first()  # Получаем пользователя по email

            # Проверяем код подтверждения и его действительность
            if user and user.verification_code == code and is_code_valid(user.code_created_at):
                user.is_active = True  # Активируем пользователя
                user.verification_code = ''  # Очищаем код
                user.code_created_at = None  # Очищаем время создания кода
                user.save()
                return redirect('main:main')  # Перенаправляем на домашнюю страницу после успешной верификации
            else:
                messages.error(request, 'Неверный или истекший код подтверждения.')
        return render(request, 'users:verification', {'form': form})

class ResendCodeView(View):
    """
    Представление для повторной отправки кода подтверждения.
    """
    def get(self, request):
        form = ResendCodeForm()
        return render(request, 'users:resend', {'form': form})

    def post(self, request):
        form = ResendCodeForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=request.user.email).first()  # Получаем пользователя по email
            
            if user:
                now = timezone.now()
                # Проверяем, прошло ли больше минуты с последнего запроса кода
                if user.last_code_request_at and (now - user.last_code_request_at).total_seconds() < 60:
                    messages.error(request, 'Вы можете запросить новый код только после истечения одной минуты.')
                else:
                    user.verification_code = generate_verification_code()  # Генерируем новый код
                    user.code_created_at = now  # Устанавливаем текущее время
                    user.last_code_request_at = now  # Обновляем время последнего запроса
                    user.save()
                    
                    # Отправка email с новым кодом
                    send_mail(
                        'Ваш новый код подтверждения',
                        f'Ваш новый код подтверждения: {user.verification_code}',
                        None,  # Используется адрес отправителя из настроек Django
                        [user.email],  # Адрес получателя
                        fail_silently=False,
                    )
                    messages.success(request, 'Новый код подтверждения отправлен на вашу почту.')
                    return redirect('users:verification')  # Перенаправление к форме ввода кода
        return render(request, 'users:resend', {'form': form})
    
class RecoveryView(View):
    """
    Представление для восстановления пароля.
    """
    def get(self, request):
        return render(request, 'users:recovery')
