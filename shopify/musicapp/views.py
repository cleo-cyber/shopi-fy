from django.shortcuts import render,redirect
from django.views import generic
from musicapp.models import Tracks,Tour
from musicapp.forms import *
from django.contrib import messages
# Create your views here.

upcoming_events=[
    {   'event_detail':'Live show',
        'date':'21 jan 2022',
        'location':'Nairobi',
        'Venue':'Carnivore',
        'Tickets':'$20',
        'description':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab enim perferendis, doloremque esse.'
    

    },
        {
        'event_detail':'Virtual show',
        'date':'21 Feb 2023',
        'location':'Mombasa',
        'Venue':'Magharibi',
        'Tickets':'$19',
        'description':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab enim perferendis, doloremque esse.'

    },
    {  'event_detail':'Inperson show',
        'date':'1 Dec 2023',
        'location':'Tanzania',
        'Venue':'Diani',
        'Tickets':'$50',
        'description':'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab enim perferendis, doloremque esse.'

    },
]
shopitems=[{
    'itemimage':'static/images/sumsung.jpg',
    'name':'EarPods',
    'price':'$20.'
},
{
    'itemimage':'static/images/headphone.jpg',
    'name':'Singer',
    'price':'$50'
},
{
    'itemimage':'static/images/manager.avif',
    'name':'Suit',
    'price':'$70'
},
{
    'itemimage':'static/images/philips.jpg',
    'name':'Philips Earpods',
    'price':'$20'
}

]

# ===== DISPLAY METHODS ===== #  
class IndexView(generic.ListView):
    template_name= 'musicapp/index.html'
    context_object_name='tracks'

    def get_queryset(self):
        context=Tracks.objects.all()
        print(context)
        return context
class TourView(generic.ListView):
    template_name='musicapp/tour.html'
    context_object_name='tours'

    def get_queryset(self):
        context=Tour.objects.all()
        print(context)
        return context


class ShopView(generic.ListView):
    template_name='musicapp/shop.html'
    context_object_name='shopitems'
    def get_queryset(self):
       return shopitems

# ===== POST METHODS ===== #
def add_track(request):
    submitted=False
    form=ImageForm()
    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            track=Tracks()
            track.track_banner=request.FILES['track_banner']
            track.title=request.POST.get('title')

            track.save()
            messages.success(request,'Product added successfully')
            return redirect('index')
    return render(request,'musicapp/add_tracks.html',{'form':form})


def add_tour(request):
    submitted=False
    form=TourForm()
    if request.method=='POST':
        form=TourForm(request.POST)
        if form.is_valid():
            newtour=Tour()
            newtour.event_description=request.POST.get('event_description')
            newtour.venue=request.POST.get('venue')
            newtour.price=request.POST.get('price')
            newtour.event_type=request.POST.get('event_type')
            newtour.save()
            return redirect('tours')

    return render(request,'musicapp/add_tour.html',{'form':form})

def admin(request):
    return render(request,'admin.html')