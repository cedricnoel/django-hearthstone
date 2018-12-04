from django.forms import ModelForm
from .models import Subject, Comment, Answer

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = [
            'title',
            'subtitle',
            'content'
        ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = [
            'content'
        ]