from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404
from .models import Card, Card_quantity

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_cards'

    def get_queryset(self):
        return Card.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'

@login_required
def my_cards(request):
    user = request.user
    all_cards = get_list_or_404(Card_quantity, owner = user)
    return render(request,'cards/my_cards.html', {'my_cards': all_cards })