from django.db import models
from datetime import datetime    

# Create your models here.
class Packet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.IntegerField(default=100)
    card_number = models.IntegerField(default=8)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    