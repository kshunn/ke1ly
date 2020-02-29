from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from pages.views import main


def aboutus(request):
    return render(request, 'aboutus.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['pw']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Username or password is incorrect')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def signup(request):
    if request.method == "POST":
        if request.POST["pw1"] == request.POST["pw2"]:
            user = User.objects.create_user(
                username=request.POST["id"], password=request.POST["pw1"])
            messages.success(request, 'Sign up successful')
            return render(request, 'login.html')
        messages.error(request, 'Confirm your password')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

