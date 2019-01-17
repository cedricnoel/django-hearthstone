from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('', views.index, name='index'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('cards/<int:pk>', views.cards, name="social_cards"),
    path('decks/<int:pk>', views.decks, name="social_decks")
]