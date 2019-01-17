from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class social(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow")

    def __str__(self):
        return self.user.username + "-" + self.follow.username

