from django.shortcuts import render, redirect
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

def new(request):
    if request.user.is_authenticated:
        return render(request, 'decks/new.html')
    else:
        return redirect('user:login')

def store(request):
    if request.user.is_authenticated and request.POST:
        deck_name = request.POST['name']
        current_user = get_current_authenticated_user()

        deck = Deck.objects.create()
        deck.owner = current_user
        deck.name = deck_name
        deck.save()

        return redirect('decks:index')
    else:
        return redirect('user:login')

def edit(request, deck_id):
    deck = Deck.objects.get(id = deck_id)

    return render(request, 'decks/edit.html', {
        'deck': deck
    })

def update(request, deck_id):
    if request.user.is_authenticated:
        Deck.objects.filter(id = deck_id).update(name = request.POST['name'])

    return redirect('decks:index')

def delete(request, deck_id):
    #current_user = get_current_authenticated_user()
    deck = Deck.objects.get(id = deck_id)
    deck.delete()

    return redirect('decks:index')