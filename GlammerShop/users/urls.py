from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('recovery/', views.recovery, name='recovery'),
    path('profile/', views.login, name='profile'),
    path('logout/', views.logout, name='logout'),
]