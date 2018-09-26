from django.shortcuts import render
from django.http import HttpResponse

from .models import Card

# Create your views here.

def index(request):
    latest_cards = Card.objects.order_by('-pub_date')[:5]
    context = {'latest_cards': latest_cards}

    return render(request, 'cards/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at card %s." % question_id)