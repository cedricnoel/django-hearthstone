from django.urls import path

from . import views

app_name = 'decks'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /deck/5/
    path('<int:deck_id>/', views.details, name='detail'),
]