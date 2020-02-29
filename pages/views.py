from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Photo
from django.utils import timezone
from .forms import PhotoForm
from .forms import EditForm


# Create your views here.
def about(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'about.html')


def main(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'main.html', {'photos': photos})


def team(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'team.html')


def addphoto(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date = timezone.now()
            post.save()
            return main(request)

    else:
        form = PhotoForm()
        return render(request, 'add.html', {'form': form})


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
        form = EditForm(request.POST)
        if form.is_valid():
            photo.title = form.cleaned_data['title']
            photo.save()
            return main(request)

    else:
        form = EditForm(instance=photo)
        return render(request, 'edit.html', {'form': form})


