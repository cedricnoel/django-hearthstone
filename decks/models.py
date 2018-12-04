import datetime

from django.db import models
from django_currentuser.db.models import CurrentUserField

class Deck(models.Model):
    owner = CurrentUserField()
    name = models.CharField(default = 'My Deck', max_length = 255)
    items = models.ManyToManyField('cards.Card', related_name="decks", blank=True)
    pub_date = models.DateTimeField(default = datetime.datetime.now(), blank = True)

    def __str__(self):
        return self.name