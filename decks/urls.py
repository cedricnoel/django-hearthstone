from django.urls import path

from . import views

app_name = 'decks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:deck_id>/', views.details, name='detail'),
    path('new/', views.new, name='new'),
    path('store/', views.store, name='store'),
    path('<int:deck_id>/edit', views.edit, name='edit'),
    path('<int:deck_id>/update', views.update, name='update'),
    path('<int:deck_id>/delete', views.delete, name='delete'),
    path('<int:deck_id>/add_cards', views.add_cards, name='add-cards'),
    path('add_deck_cards', views.add_deck_cards, name='add-deck-cards'),
    path('remove_deck_cards', views.remove_card, name='remove-deck-cards'),
]