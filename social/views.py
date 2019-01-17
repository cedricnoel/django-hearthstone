from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import social

@login_required
def index(request):
    all_user = list(User.objects.all())
    user = request.user
    try:
        my_follow = social.objects.all().filter(user=user)
    except:
        my_follow = None
    
    if my_follow is not None:
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
    social.objects.create(user=request.user, follow=follower)
    return HttpResponseRedirect("/social")