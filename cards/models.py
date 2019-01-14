from django.db import models
from django.contrib.auth.models import User
from decks.models import Deck
from colorfield.fields import ColorField

class Type(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

class Card(models.Model):
    #owners = models.ManyToManyField("User", related_name="cards", through="CardQuantity")
    name = models.CharField(max_length=200)
    life = models.IntegerField(default=1)   
    atk = models.IntegerField(default=1)
    cost = models.IntegerField(default=0)
    deck = models.ManyToManyField(Deck, related_name="cards", blank=True)
    desc = models.TextField()
    type = models.ManyToManyField(Type)
    image = models.ImageField(upload_to = 'cards/static/img/', default = 'cards/static/img/no-img.jpg')
    pub_date = models.DateTimeField('date published')
    owners = models.ManyToManyField(User, related_name="cards", blank=True, through="Card_quantity")

    def __str__(self):
        return self.name

class Card_quantity(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.card.name + "_" + self.owner.username