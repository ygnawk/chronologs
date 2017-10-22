from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def index(request):
    return render(request, 'register/index.html')


def login_page(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        success = True
    else:
        success = False

    return render(request, 'register/loggedin.html', {
        'username': username, 
        'success' : success
    })


def register(request):
    return render(request, 'register/register.html')


def submit(request):
    email    = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']

    fname    = request.POST['fname']
    lname    = request.POST['lname']

    try:
        user = User.objects.create_user(
                email=email,
                username=username,
                password=password,
                first_name=fname,
                last_name=lname)

        user.save()

        success = True

    except IntegrityError:
        success = False

    if 'next' in request.POST:
        return HttpResponseRedirect(request.POST['next'])
    else:
        return render(request, 'register/index.html')


def logout_page(request):
    username = request.user.username
    logout(request)
    return render(request, 'register/loggedout.html', {'username' : username } )
