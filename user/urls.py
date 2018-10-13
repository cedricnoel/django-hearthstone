from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registerAction/', views.registerAction, name="registerAction"),
    path('loginAction/', views.loginAction, name='loginAction'),
    path('logoutAction/', views.logoutAction, name="logoutAction")
]