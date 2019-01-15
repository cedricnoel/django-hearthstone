from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    all_user = User.objects.all()
    return render(request,'challenge/index.html', {"all_user": all_user})

def challenge_request(request, challenger_id):
    return render(request, 'challenge/challenge_index.html', {"challenger_id": challenger_id})