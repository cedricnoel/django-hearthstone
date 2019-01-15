from django.urls import path

from . import views

app_name = 'challenge'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:challenger_id>/', views.challenge_request, name='challenge_request')
]