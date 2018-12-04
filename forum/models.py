import datetime

from django.db import models
from user.models import User

class Subject(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(default='', max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subjects")
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="comments")
    pub_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return 'Commentaire de ' + self.author.username

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    content = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return 'Réponse de ' + self.author.username

class Action(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actions")
    content = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return 'Action de ' + self.author.username
