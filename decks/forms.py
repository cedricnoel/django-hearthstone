from decks.models import Deck
from django.forms import ModelForm

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['name', 'items']
