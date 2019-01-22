from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

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
        path('profile/editAction', views.profile_edit_action, name="profile_edit_action"),
        path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset_form.html'), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('reset/done', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
    ]))
]