from django.shortcuts import render, get_object_or_404
from cards.models import Card
from .models import Packet
from cards.models import Card_quantity
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
            cards.append(card)
            if Card_quantity.objects.filter(card = card, owner = user).exists() :
                My_Card_quantity = Card_quantity.objects.get(card = card, owner = user)
                My_Card_quantity.quantity = My_Card_quantity.quantity +1
                My_Card_quantity.save()
            else:
               new_card_quantity = Card_quantity(card = card, owner = user, quantity = 1)
               new_card_quantity.save()
        user.profile.card_count = user.profile.card_count + packet.card_number
        user.profile.points = user.profile.points - packet.cost
        user.profile.save()
        return render(request,'packet/showCards.html', {'cards': cards, "error": ""},)

@login_required
def index(request):
    packets = Packet.objects.order_by('cost')
    return render(request,'packet/index.html', {'packets': packets})