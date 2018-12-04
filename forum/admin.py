from django.contrib import admin
from .models import Subject, Comment, Answer, Action

admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Answer)
admin.site.register(Action)
