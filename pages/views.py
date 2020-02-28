from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Photo
from django.utils import timezone


# Create your views here.
def about(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'about.html')


def main(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    photos = Photo.objects
    return render(request, 'main.html', {'photos': photos})


def team(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'team.html')


def add(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'add.html')


def addphoto(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    photo = Photo()
    photo.category = request.GET['category']
    photo.title = request.GET['title']
    photo.body = request.GET['body']
    photo.date = timezone.datetime.now()
    photo.save()
    return main(request)


def deletephoto(request, photo_id):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    photo = Photo.objects.get(id=photo_id)
    photo.delete()
    return main(request)


def editphoto(request, photo_id):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    photo = Photo.objects.get(id=photo_id)
    if request.method == "POST":
        photo.category = request.POST['category']
        photo.title = request.POST['title']
        photo.body = request.POST['body']
        photo.save()
        return main(request)

    else:
        return render(request, 'edit.html')


