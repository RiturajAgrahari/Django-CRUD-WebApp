from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='Login'),
    path('logout/', views.logout_user, name='Logout'),
]