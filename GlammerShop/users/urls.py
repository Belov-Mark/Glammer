from django.urls import path

from users import views

from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('verification/', views.VerifyCodeView.as_view(), name='verification'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('resend_code/', views.ResendCodeView.as_view(), name='resend_code'),
    path('recovery/', views.RecoveryView.as_view(), name='recovery'),
]
