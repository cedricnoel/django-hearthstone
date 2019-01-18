from django.urls import path

from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('my_cards', views.my_cards, name='my_cards'),
    path('cards_sell/<int:pk>', views.cards_sell, name="cards_sell")
]