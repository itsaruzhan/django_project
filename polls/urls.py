"""my_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('create_clothes', views.create_clothes),
    path('show_clothes', views.show_clothes, name= 'show_clothes'),
    path('update_clothes/<int:id>', views.update_clothes),
    path('delete_clothes/<int:id>', views.delete_clothes),

    path('create_customs', views.create_customs),
    path('show_customs', views.show_customs, name= 'show_customs'),
    path('update_customs/<int:id>', views.update_customs),
    path('delete_customs/<int:id>', views.delete_customs),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
