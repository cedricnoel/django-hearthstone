from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Card, Card_quantity
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_cards'

    def get_queryset(self):
        return Card.objects.order_by('name')

def detail(request, pk):
    user = request.user
    card = get_object_or_404(Card, pk=pk)
    user_card = get_object_or_404(Card_quantity, owner = user, card=card)
    if user_card.quantity >0:
        return render(request, 'cards/detail.html', {
            'card': user_card,
            'user': user
        })
    else:
        return HttpResponseRedirect("/cards/my_cards")

@login_required
def my_cards(request):
    user = request.user
    all_cards = Card_quantity.objects.filter(owner=user)
    return render(request,'cards/my_cards.html', {'my_cards': all_cards })

@login_required
def cards_sell(request, pk):
    quantity = int(request.POST.get('quantity'))
    card = get_object_or_404(Card, pk=pk)
    user = request.user
    user_card =  get_object_or_404(Card_quantity, owner = user, card=card)

    if user.profile.card_count <= 20 or user.profile.card_count - quantity <= 20:
        return render(request, 'cards/detail.html', {
                'card': user_card,
                'Message' : 'Nombre de carte insuffisante, vous devez avoir minimum 20 cartes dans votre collection.',
        })
    
    if quantity <= user_card.quantity and user_card.quantity > 0:
        user_card.quantity = user_card.quantity - quantity
        user.profile.points = user.profile.points + (card.cost*10)*quantity
        user.profile.save()
        user_card.save()

        if user_card.quantity > 0 :
            return render(request, 'cards/detail.html', {
                'card': user_card,
                'Message' : str(quantity) + 'x ' + str(card.name) + ' a été vendu',
            })
        else:
            all_cards = Card_quantity.objects.filter(owner=user)
            return render(request,'cards/my_cards.html', {'my_cards': all_cards }) 
    else:
         return render(request, 'cards/detail.html', {
        'card': user_card,
        'Message' : 'Quantité invalid',
    }) 