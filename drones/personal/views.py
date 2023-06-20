from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from account.models import Account


def home_screen(request):
    context={}
    accounts=Account.objects.all()
    context['accounts'] = accounts
    
    return render(request,'personal/home.html',context)

