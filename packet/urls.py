from django.urls import path

from . import views

app_name = 'packet'
urlpatterns = [
    path('open_packet', views.open_packet, name='open'),
    path('', views.index, name="index")
]