from django.shortcuts import render
from .models import Subject

def index(request):
    subjects = Subject.objects.all()

    return render(request, 'forum/index.html', {
        'subjects': subjects
    })
