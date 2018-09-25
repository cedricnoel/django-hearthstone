from django.db import models

class Type(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Card(models.Model):
    name = models.CharField(max_length=200)
    life = models.IntegerField(default=1)
    atk = models.IntegerField(default=1)
    cost = models.IntegerField(default=0)
    descr = models.TextField()
    pub_date = models.DateTimeField('date published')