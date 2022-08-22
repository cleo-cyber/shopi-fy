from django.shortcuts import render, redirect
from django.views import generic
from musicapp.models import Tracks, Tour
from musicapp.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class TourView(generic.ListView):
    template_name = 'musicapp/tour.html'
    context_object_name = 'tours'

    def get_queryset(self):
        context = Tour.objects.all()
        return context


def add_tour(request):

    try:
        form = TourForm()
        if request.method == 'POST':
            form = TourForm(request.POST)
            if form.is_valid():
                newtour = Tour()
                newtour.event_description = request.POST.get(
                    'event_description')
                newtour.venue = request.POST.get('venue')
                newtour.price = request.POST.get('price')
                newtour.event_type = request.POST.get('event_type')
                newtour.save()
                return redirect('tours')
        else:
            form = TourForm()
    except:
        ValueError('Enter valid data')

    return render(request, 'musicapp/add_data/add_tour.html', {'form': form})
