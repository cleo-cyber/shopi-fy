from django.shortcuts import render, redirect
from django.views import generic
from musicapp.models import Tracks, Tour
from musicapp.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class IndexView(generic.ListView):
    template_name = 'musicapp/index.html'
    context_object_name = 'tracks'
    

    def get_queryset(self):
        context = Tracks.objects.all()
        return context


class AdminViewTracks(generic.ListView):
    template_name = 'musicapp/admin/displaydata/admin_tracks.html'
    context_object_name = 'tracks'

    def get_queryset(self):
        context = Tracks.objects.all()
        return context


@login_required
def add_track(request):
    form = ImageForm()
    try:
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                track = Tracks()
                track.track_banner = request.FILES['track_banner']
                track.title = request.POST.get('title')

                track.save()
                messages.success(request, 'Product added successfully')
                return redirect('admintracks')
    except:
        ValidationErr('Inavlid data')
    return render(request, 'musicapp/add_data/add_tracks.html', {'form': form})


def edit_track(request, pk):
    try:
        track = Tracks.objects.get(pk=pk)
        form = ImageForm(request.POST or None, instance=track)
        if form.is_valid():
            form.save()
            return redirect('admintracks')
    except:
        print('update error')
    return render(request, 'musicapp/update/update_track.html', {'track': track,
                                                                 'form': form})

# ===== DELETE ==== #


def remove_track(request, pk):
    try:
        track = Tracks.objects.get(pk=pk)
        track.delete()
        print('delete successfull')
        return redirect('admintracks')
    except:
        ValueError('Invalid operation')
    return render(request, 'musicapp/update/update_track.html')
