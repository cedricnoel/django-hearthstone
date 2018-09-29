from django.contrib import admin

from .models import Type, Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')

admin.site.register(Type)
admin.site.register(Card, CardAdmin)
