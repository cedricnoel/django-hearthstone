from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

# Create your views here.

# -------- GET TEMPLATE --------
def login(request):
    return render(request,'user/login.html')

def register(request):
    return render(request, 'user/register.html')

# -------- POST ACTION --------

def loginAction(request):
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