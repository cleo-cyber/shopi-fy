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
def hello(request):

    context={'tracks':tracks}
    return render(request,'index.html',context)