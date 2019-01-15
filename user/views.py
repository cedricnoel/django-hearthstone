from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

# -------- GET TEMPLATE --------
def login(request):
    if request.user.is_authenticated:
        # Change later for homepage
        return redirect("cards:index")
    else:    
        return render(request,'user/login.html')

def register(request):
    return render(request, 'user/register.html')


@login_required
def profile(request):
    return render(request, "user/profile.html")

@login_required
def profile_edit(request):
    return render(request, "user/profile_edit.html")

# -------- POST ACTION --------

def loginAction(request):
    if request.user.is_authenticated:
        # Change later for homepage
        return redirect("user:login")
    else:    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            #Maybe change it later for dashboard
            return redirect("cards:index")
        else:
            return render(request, 'user/login.html', {
                'error_message': "Bad credentials.",
            })

def registerAction(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect("user:login")

def logoutAction(request):
    logout(request)
    # Change later for homepage
    return redirect("user:login")

def profile_edit_action(request):
    if request.user.is_authenticated:
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        return redirect("User:profile")