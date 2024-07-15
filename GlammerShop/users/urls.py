from django.urls import path

from users import views

app_name = 'user'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signin/', views.UserSigninView.as_view(), name='signin'),
    path('verification/', views.VerifyCodeView.as_view(), name='verification'),
    path('recovery/', views.recovery, name='recovery'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]