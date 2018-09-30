from django.views import generic

from .models import Card

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_cards'

    def get_queryset(self):
        return Card.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Card
    template_name = 'cards/detail.html'
