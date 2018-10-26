from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'user'
urlpatterns = [
    url('accounts/', include([
        path('login/', views.login, name='login'),
        path('register/', views.register, name='register'),
        path('registerAction/', views.registerAction, name="registerAction"),
        path('loginAction/', views.loginAction, name='loginAction'),
        path('logout/', views.logoutAction, name="logoutAction"),
        path('profile/', views.profile, name="profile"),
        path('profile/edit', views.profile_edit, name="profile_edit"),
        path('profile/editAction', views.profile_edit_action, name="profile_edit_action")
    ])),
]