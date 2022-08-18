from django.shortcuts import render,redirect
from django.views import generic
from musicapp.models import Tracks,Tour
from musicapp.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.


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
@login_required
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
    return render(request,'musicapp/add_data/add_tracks.html',{'form':form})

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
    else:
        form=TourForm()

    return render(request,'musicapp/add_data/add_tour.html',{'form':form})

    

# ==== User Accounts ==== #

def registration_view(request):
    context={}
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form']=form

    else:#get request
        form=RegistrationForm()
        context['register_form']=form

    return render(request,'musicapp/admin/registration.html',context)


def login_view(request):
    context={}
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']

            user=authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('admin')
        else:
            context['login_form']=form
    else:
        form=UserLoginForm()
        context['login_form']=form

    return render(request,'musicapp/admin/login.html',context)


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def admin(request):
    
    return render(request,'admin.html')
# TODO -ASSIGNING PERMISSIONS