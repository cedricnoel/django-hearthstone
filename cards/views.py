from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Card

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_cards'

    def get_queryset(self):
        return Card.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'

@login_required
def my_cards(request):
    user = request.user
    return render(request,'cards/my_cards.html', {'my_cards': user.cards.all() })