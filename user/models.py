from django.db import models
from cards.models import Card
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=1000)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


