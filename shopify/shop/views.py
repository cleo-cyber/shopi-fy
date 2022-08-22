from django.shortcuts import render
from django.views import generic

# Create your views here.
shopitems = [{
    'itemimage': 'static/images/sumsung.jpg',
    'name': 'EarPods',
    'price': '$20.'
},
    {
    'itemimage': 'static/images/headphone.jpg',
    'name': 'Singer',
    'price': '$50'
},
    {
    'itemimage': 'static/images/manager.avif',
    'name': 'Suit',
    'price': '$70'
},
    {
    'itemimage': 'static/images/philips.jpg',
    'name': 'Philips Earpods',
    'price': '$20'
}

]

# ===== DISPLAY METHODS ===== #
class ShopView(generic.ListView):
    template_name = 'musicapp/shop.html'
    context_object_name = 'shopitems'

    def get_queryset(self):
        return shopitems