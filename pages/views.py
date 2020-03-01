from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Photo
from django.utils import timezone
from .forms import PhotoForm
from .forms import EditForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages


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
            return redirect('main')

    else:
        form = PhotoForm()
        return render(request, 'add.html', {'form': form})


def deletephoto(request, photo_id):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    photo = Photo.objects.get(id=photo_id)
    photo.delete()
    return redirect('main')


def editphoto(request, photo_id):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    photo = Photo.objects.get(id=photo_id)
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            photo.title = form.cleaned_data['title']
            photo.save()
            return redirect('main')

    else:
        form = EditForm(instance=photo)
        return render(request, 'edit.html', {'form': form})


def settings(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render(request, 'settings.html')


def changepw(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    if request.method == "POST":
        current_password = request.POST.get("opw")
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST.get("npw1")
            password_confirm = request.POST.get("npw2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password change successful')
                return redirect('login')
            else:
                messages.error(request, 'Confirm your new password')
                return render(request, 'changepw.html')
        else:
            messages.error(request, 'Incorrect original password')
            return render(request, 'changepw.html')

    return render(request, 'changepw.html')


def withdrawal(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    if request.method == "POST":
        pw1 = request.POST.get("pw1")
        if check_password(pw1, request.user.password):
            request.user.delete()
            messages.success(request, 'Withdrawal successful')
            return redirect('login')
        else:
            messages.error(request, 'Incorrect password')
            return render(request, 'withdrawal.html')

    return render(request, 'withdrawal.html')
