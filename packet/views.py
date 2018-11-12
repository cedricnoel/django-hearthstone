from django.shortcuts import render
from cards.models import Card
from .models import Packet
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def open_packet(self, packet_id):
    packet =  get_object_or_404(Packet, pk=packet_id)
    cards = Card.objects.order_by('-pub_date')[:packet.card_number]
    return HttpResponse(cards)

@login_required
def index(request):
    packets = Packet.objects.order_by('-pub_date')
    return render(request,'packet/index.html', {'packets': packets})