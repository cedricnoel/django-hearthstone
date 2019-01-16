from django.shortcuts import render, redirect
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

from cards.models import Card
from .models import Deck
from .forms import DeckForm

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
        cards = Card.objects.all()

        form = DeckForm()

        return render(request, 'decks/new.html', {
            'cards': cards,
            'form': form
        })
    else:
        return redirect('user:login')

def store(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = DeckForm(request.POST)

        if form.is_valid():
            deck = form.save()

            return redirect('decks:detail', deck_id = deck.id)

        return redirect('decks:index')
    else:
        return redirect('user:login')

def edit(request, deck_id):
    deck = Deck.objects.get(id = deck_id)
    form = DeckForm(instance=deck)

    return render(request, 'decks/edit.html', {
        'deck': deck,
        'form': form
    })

def update(request, deck_id):
    if request.user.is_authenticated and request.method == 'POST':
        deck = Deck.objects.get(pk=deck_id)
        form = DeckForm(request.POST, instance=deck)

        if form.is_valid():
            form.save()

            return redirect('decks:detail', deck_id=deck.id)

    return redirect('decks:index')

def delete(request, deck_id):
    #current_user = get_current_authenticated_user()
    deck = Deck.objects.get(id = deck_id)
    deck.delete()

    return redirect('decks:index')