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
def open_packet(self, packet_id):
    #TODO: Check if user is connected and if he has enough points
    packet =  get_object_or_404(Packet, pk=packet_id)
    count = Card.objects.count()
    all_cards = Card.objects.all()
    user = get_current_user()
    cards = []
    for k in range(0, packet.card_number):
        cards.append(all_cards[randint(0, count - 1)])
    return HttpResponse(cards)


@login_required
def index(request):
    packets = Packet.objects.order_by('-pub_date')
    return render(request,'packet/index.html', {'packets': packets})