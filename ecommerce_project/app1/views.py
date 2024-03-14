from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    products = Ecommerce_Product.objects.all()
    context = {
        'products' : products
    }
    return render(request,'app1/index.html', context)


def login_user(request):

    return render(request,'app1/login.html', )


def logout_user(request):
    pass
