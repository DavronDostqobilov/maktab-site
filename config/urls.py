"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# urls.py
# urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from register import views

urlpatterns = [
    path('badmin/', admin.site.urls),
    path('', views.kirish, name='home'),  # Asosiy sahifa
    path('register/', views.ruyxat, name='register'),  # Register sahifasi
    path('main.html/', views.main, name='main'),  # Main sahifasi
    path('akkauntbor', views.akkauntbor, name='akkauntbor'),
    path('ustozlar/', views.ustoz, name='ustozlar'),
    path('resurslar/', views.resurslar, name='resurslar'),
    path('o`uvchilar/', views.uquv, name='o`uvchilar'),
    path('bog`lanish/', views.boglan, name='bog`lanish'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
