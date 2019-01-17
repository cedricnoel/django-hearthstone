import random

from challenge.models import Challenge
from decks.models import Deck, Deck_cards
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def index(request):
    all_user = User.objects.all()
    decks = Deck.objects.filter(owner=request.user)

    return render(request, 'challenge/index.html', {
        "all_user": all_user,
        'decks': decks
    })

@login_required
def challenge_request(request):
    challenger = request.user
    deck1 = Deck.objects.get(pk=int(request.POST['deck1']))
    challenged = User.objects.get(pk=int(request.POST['challenger_id']))

    challenge = Challenge(
        player1=challenger,
        deck1=deck1,
        player2=challenged
    )
    challenge.save()

    return redirect('challenge:challenge_list')

@login_required
def challenge_list(request):
    challenging = request.user.challenger.filter(status='pending') # Current user challenged them
    challenged = request.user.challenged.filter(status='pending')  # They challenged current user
    decks = Deck.objects.filter(owner=request.user)

    return render(request, 'challenge/list.html', {
        'challenging': challenging,
        'challenged': challenged,
        'decks': decks
    })

@login_required
def fight(request, challenge_id):
    if request.method == 'POST':
        challenge = Challenge.objects.get(pk=challenge_id)

        game = {
            #'deck1': sorted(challenge.deck1.items.all(), key=lambda y: random.random()),
            'newDeck1': sorted(Deck_cards.objects.filter(deck=challenge.deck1), key=lambda y: random.random()),
            #'deck2': sorted(Deck.objects.get(pk=request.POST['deck']).items.all(), key=lambda y: random.random()),
            'newDeck2': sorted(Deck_cards.objects.filter(deck=request.POST['deck']), key=lambda y: random.random()),
            'lp1': 100,
            'lp2': 100,
            'winner': ''
        }

        for x in range(0, 10):
            if x % 2 == 0 and x < len(game['newDeck1']) and x < len(game['newDeck2']):
                result = do_battle(game['newDeck1'][x].card, game['newDeck1'][x].card)
                # You win
                if result == 1:
                    game['lp2'] -= game['newDeck1'][x].card.atk - game['newDeck2'][x].card.atk
                # You lose
                if result == 2:
                    game['lp1'] -= game['newDeck2'][x].card.atk - game['newDeck1'][x].card.atk

            if x % 2 > 0 and x < len(game['newDeck1']) and x < len(game['newDeck2']):
                result = do_battle(game['newDeck2'][x].card, game['newDeck1'][x].card)
                # He win
                if result == 1:
                    game['lp1'] -= game['newDeck2'][x].card.atk - game['newDeck1'][x].card.atk
                # He lose
                if result == 2:
                    game['lp2'] -= game['newDeck1'][x].card.atk - game['newDeck2'][x].card.atk

        if game['lp1'] > game['lp2']:
            game['winner'] = challenge.player1.username

            challenge.player1.profile.victory += 1
            challenge.player1.profile.save()

            challenge.player2.profile.defeat += 1
            challenge.player2.profile.save()

            challenge.status = 'win'

        elif game['lp1'] < game['lp2']:
            game['winner'] = challenge.player2.username

            challenge.player2.profile.victory += 1
            challenge.player2.profile.save()

            challenge.player1.profile.defeat += 1
            challenge.player1.profile.save()

            challenge.status = 'lose'

        else:
            game['winner'] = 'nobody'

            challenge.status = 'equality'
            challenge.save()

        return HttpResponse(
            'Turn: ' + str(x) +
            ', result: ' + str(result) +
            ', lp1: ' + str(game['lp1']) +
            ', lp2: ' + str(game['lp2']) +
            ', winner: ' + game['winner']
        )

def do_battle(card1, card2):
    if card1.atk > card2.atk:
        return 1

    if card1.atk < card2.atk:
        return 2

    return 3

def decline_challenge(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    challenge.status = 'declined'
    challenge.save()

    return redirect('challenge:challenge_list')