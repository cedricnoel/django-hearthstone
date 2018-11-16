from django.db import models

from decks.models import Deck

class Type(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=200)
    life = models.IntegerField(default=1)
    atk = models.IntegerField(default=1)
    cost = models.IntegerField(default=0)
    deck = models.ForeignKey(Deck, on_delete=models.SET_NULL, null=True)
    descr = models.TextField()
    type = models.ManyToManyField(Type)
    image = models.ImageField(upload_to = 'cards/static/img/', default = 'cards/static/img/no-img.jpg')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name