from django.shortcuts import render, redirect
from django.views import generic
from musicapp.models import Tour
from musicapp.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ==== Display methods ==== #


class TourView(generic.ListView):
    template_name = 'musicapp/tour.html'
    context_object_name = 'tours'

    def get_queryset(self):
        context = Tour.objects.all()
        return context


class TourAdminList(generic.ListView):
    template_name = 'musicapp/admin/displaydata/admin_tour.html'
    context_object_name = 'tours'

    def get_queryset(self):
        context = Tour.objects.all()
        return context
# ==== Add Data Methods === #


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
                return redirect('tours-list')
        else:
            form = TourForm()
    except:
        ValueError('Enter valid data')

    return render(request, 'musicapp/add_data/add_tour.html', {'form': form})

# ====Edit Methods === #


def edit_tour(request, pk):
    try:
        
        tour = Tour.objects.get(pk=pk)
        form = TourForm(request.POST or None, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tours-list')
    except:
        ValueError('Inalid operation')
    return render(request, 'musicapp/update/update_tour.html', {'form': form,

                                                                'tour': tour})


def delete_tour(request, pk):
    tour = Tour.objects.get(pk=pk)
    tour.delete()
    return redirect('tours-list')
