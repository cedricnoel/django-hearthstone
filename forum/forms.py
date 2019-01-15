import django.forms as forms
from .models import Subject, Comment, Answer

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'title',
            'subtitle',
            'content'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'content'
        ]