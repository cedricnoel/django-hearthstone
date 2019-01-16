from django.db import models
from datetime import datetime    

# Create your models here.
class Packet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'packets/static/img/', default = 'packets/static/img/no-img.jpg')
    cost = models.IntegerField(default=100)
    card_number = models.IntegerField(default=8)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    