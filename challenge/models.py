from decks.models import Deck
from django.contrib.auth.models import User
from django.db import models

class Challenge(models.Model):
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenger')
    deck1   = models.ForeignKey(Deck, on_delete=models.DO_NOTHING, related_name='challenger_deck')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='challenged')
    deck2   = models.ForeignKey(Deck, blank=True, on_delete=models.DO_NOTHING, related_name='challenged_deck', null=True)
    status  = models.CharField(max_length=200, default='pending')
    winner  = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING, related_name='wins', null=True)
