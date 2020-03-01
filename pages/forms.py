from django import forms
from .models import Photo
from django.forms import TextInput


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'})
        }
