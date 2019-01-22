from django.urls import path
from . import views

app_name = 'challenge'
urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.challenge_request, name='challenge_request'),
    path('list/', views.challenge_list, name='challenge_list'),
    path('fight/<int:challenge_id>/', views.fight, name='fight'),
    path('decline/<int:challenge_id>/', views.decline_challenge, name='decline')
]