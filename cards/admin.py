from django.contrib import admin

from .models import Type, Card, Card_quantity

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')

admin.site.register(Type, TypeAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Card_quantity)