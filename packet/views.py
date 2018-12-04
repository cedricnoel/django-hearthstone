from django.shortcuts import render, get_object_or_404
from cards.models import Card
from .models import Packet
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from random import randint
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

# Create your views here.

@login_required
def open_packet(request, packet_id):
    user = request.user.profile.points
    packet =  get_object_or_404(Packet, pk=packet_id)
    if request.user.profile.points < packet.cost:
        return render(request,'packet/showCards.html', {'cards': [], "error": "Vous n'avez pas assez de points"},)
    else:
        count = Card.objects.count()
        all_cards = Card.objects.all()
        user = get_current_user()
        cards = []
        for k in range(0, packet.card_number):
            card = all_cards[randint(0, count - 1)]
            card.owners.add(user)
            cards.append(card)
        user.profile.points = user.profile.points - packet.cost
        user.profile.save()
        return render(request,'packet/showCards.html', {'cards': cards, "error": ""},)


@login_required
def index(request):
    packets = Packet.objects.order_by('-pub_date')
    return render(request,'packet/index.html', {'packets': packets})