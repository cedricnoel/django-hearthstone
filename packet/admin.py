from django.contrib import admin

from .models import Packet

class PacketAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')


admin.site.register(Packet, PacketAdmin)