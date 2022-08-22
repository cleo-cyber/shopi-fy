from django.shortcuts import render, redirect
from django.views import generic
from musicapp.models import Tracks, Tour
from musicapp.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.





@login_required
def admin(request):

    return render(request, 'admin.html')
# TODO -ASSIGNING PERMISSIONS
