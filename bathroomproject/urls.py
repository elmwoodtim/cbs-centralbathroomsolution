"""bathroomproject URL Configuration

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
from bathroomapp import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('register', views.register_user, name='register'),
    path('guest', views.guest, name='guest'),
    path('loggedIn', views.loggedin, name='loggedIn'),
    path('guest_data', views.guest_data, name='guest_data'),
    path('resorts', views.resort_finder, name='resorts'),
    path('admin_operations', views.do_admin_stuff, name='do_admin_stuff'),
    path('logout/', LogoutView.as_view(), name='logout')
]
