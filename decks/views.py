from django.shortcuts import render
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

from cards.models import Card
from .models import Deck

def index(request):
    current_user = get_current_authenticated_user()
    decks = Deck.objects.filter(owner=current_user)

    return render(request, 'decks/index.html', {
        'decks': decks
    })

def details(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    cards = Card.objects.filter(deck=deck_id)

    return render(request, 'decks/details.html', {
        'deck': deck,
        'cards': cards
    })
