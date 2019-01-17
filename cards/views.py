from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Card, Card_quantity
from django.http import HttpResponseRedirect, HttpResponse

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_cards'

    def get_queryset(self):
        return Card.objects.order_by('name')

def detail(request, pk):
    user = request.user
    card = get_object_or_404(Card, pk=pk)

    if not user.is_authenticated :
        return render(request, 'cards/detail.html', {
            'card': card,
            'user': False
        })
    else:
        user_card = Card_quantity.objects.get(owner = user, card=card)

        if user_card:
            return render(request, 'cards/detail.html', {
                'card': user_card.card,
                'user': user,
                'quantity': user_card.quantity
            })
        else:
            return render(request, 'cards/detail.html', {
                'card': card,
                'user': user
            })
 

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
    user_card = Card_quantity.objects.get(owner = user, card=card)

    if user.profile.card_count <= 10 or user.profile.card_count - quantity <= 10:
        return render(request, 'cards/detail.html', {
                'card': user_card.card,
                'quantity' : user_card.quantity,
                'Message' : 'Nombre de carte insuffisante, vous devez avoir minimum 10 cartes dans votre collection.',
        })

    
    if quantity <= user_card.quantity and user_card.quantity > 0:
        user_card.quantity = user_card.quantity - quantity
        user.profile.points = user.profile.points + (card.cost*10)*quantity
        user.profile.card_count = user.profile.card_count - quantity
        user.profile.save()
        user_card.save()

        if user_card.quantity > 0 :
            return render(request, 'cards/detail.html', {
                'card': user_card.card,
                'quantity' : user_card.quantity,
                'Message' : str(quantity) + 'x ' + str(card.name) + ' a été vendu',
            })
        else:
            all_cards = Card_quantity.objects.filter(owner=user)
            return render(request,'cards/my_cards.html', {'my_cards': all_cards }) 
    else:
         return render(request, 'cards/detail.html', {
        'card': user_card.card,
        'quantity' : user_card.quantity,
        'Message' : 'Quantité invalid',
    }) 