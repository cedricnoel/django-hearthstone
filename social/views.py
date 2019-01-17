from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import social
from cards.models import Card, Card_quantity

@login_required
def index(request):
    user = request.user
    all_user = list(User.objects.exclude(pk=user.id))
    try:
        my_follow = social.objects.all().filter(user=user)
    except:
        my_follow = None

    if my_follow is not None and len(my_follow) > 0:
        for follower in my_follow:
            if follower.follow in all_user:
                all_user.remove(follower.follow)

    return render(request,'social/index.html', {
        "all_user": all_user,
        "my_follow": my_follow
    })

@login_required
def follow(request, pk):
    follower = User.objects.get(pk=pk)
    try:
        social.objects.get(user=request.user, follow=follower)
        return HttpResponseRedirect("/social")
    except:
        social.objects.create(user=request.user, follow=follower)
        return HttpResponseRedirect("/social")

@login_required
def cards(request,pk):
    user = User.objects.get(pk=pk)
    my_cards = Card_quantity.objects.filter(owner=user)
    return render(request,'social/cards.html', {'my_cards': my_cards, 'user': user })