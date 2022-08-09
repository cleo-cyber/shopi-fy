from django.shortcuts import render,redirect
from django.views import generic
from musicapp.models import Tracks
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
    'price':'$20'
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

    
class IndexView(generic.ListView):
    template_name= 'musicapp/index.html'
    context_object_name='tracks'

    def get_queryset(self):
        context=Tracks.objects.all()
        print(context)
        return context
class TourView(generic.ListView):
    template_name='musicapp/tour.html'
    context_object_name='upcoming_events'

    def get_queryset(self):
        return upcoming_events


class ShopView(generic.ListView):
    template_name='musicapp/shop.html'
    context_object_name='shopitems'
    def get_queryset(self):
       return shopitems

#  POST METHODS
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