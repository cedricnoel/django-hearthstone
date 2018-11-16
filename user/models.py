from django.db import models
from cards.models import Card
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class card_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)
 

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        user.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.profile.save()


