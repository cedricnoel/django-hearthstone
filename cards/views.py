from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Card

def index(request):
    try:
        latest_cards = Card.objects.order_by('-pub_date')[:5]
    except:
        raise Http404("Question does not exist")

    context = {'latest_cards': latest_cards}

    return render(request, 'cards/index.html', context)


def detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    context = {'card': card}

    return render(request, 'cards/detail.html', context)
