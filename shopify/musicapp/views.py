from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

tracks=[{
'id':1,
'image_link':'static/images/golden.jpg ',
'name':'Katelele'

},
{
'id':2,
'image_link':'static/images/jbl.avif',
'name':'Casset'

},
{
'id':3,
'image_link':'static/images/pods.jpg',
'name':'Tape'

},
{
'id':4,
'image_link':'static/images/headphone.jpg',
'name':'Fan'

},
{
'id':5,
'image_link':'static/images/philips.jpg',
'name':'Catalogue'

}
]
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


def index(request):
    
    context={'tracks':tracks}
    return render(request,'musicapp/index.html',context)

def tours(request):
    context={'upcoming_events':upcoming_events}
    return render(request,'musicapp/tour.html',context)