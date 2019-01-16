import datetime

from django.db import models
from django_currentuser.db.models import CurrentUserField

class Deck(models.Model):
    owner = CurrentUserField()
    name = models.CharField(default = 'My Deck', max_length = 255)
    pub_date = models.DateTimeField(default = datetime.datetime.now(), blank = True)
    def __str__(self):
        return self.name

class Deck_cards(models.Model):
    card = models.ForeignKey("cards.Card", on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.deck.name + "-" + self.card.name
