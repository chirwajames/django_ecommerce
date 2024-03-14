from django.contrib.auth import admin
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name="index"),
    path('home/', views.index, name="index"),
    path('login/',views.login_user, name="login"),
    path('logout/', views.logout_user,name="logout")
]