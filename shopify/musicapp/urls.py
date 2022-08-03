from django.urls import path
from musicapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('tours/',views.tours,name='tours')
]