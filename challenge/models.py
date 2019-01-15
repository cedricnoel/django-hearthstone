from decks.models import Deck
from django.contrib.auth.models import User
from django.db import models

class Challenge(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE)
    deck1   = models.ForeignKey(Deck)
    player2 = models.ForeignKey(User, on_delete=models.CASCADE)
    deck2   = models.ForeignKey(Deck, blank=True)
    status  = models.CharField(choices=['pending', 'accepted', 'declined'], default='pending')
    winner  = models.ForeignKey(User, blank=True)
