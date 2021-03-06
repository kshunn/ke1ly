"""ke1ly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import accounts.views
import pages.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('signup/', accounts.views.signup, name='signup'),
    path('aboutus/', accounts.views.aboutus, name='aboutus'),
    path('main/', pages.views.main, name='main'),
    path('about/', pages.views.about, name='about'),
    path('team/', pages.views.team, name='team'),
    path('addphoto/', pages.views.addphoto, name='addphoto'),
    path('deletephoto/<int:photo_id>/', pages.views.deletephoto, name='deletephoto'),
    path('editphoto/<int:photo_id>/', pages.views.editphoto, name='editphoto'),
    path('settings/', pages.views.settings, name='settings'),
    path('changepw/', pages.views.changepw, name='changepw'),
    path('withdrawal/', pages.views.withdrawal, name='withdrawal'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
