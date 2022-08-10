from django.urls import path
from musicapp import views

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('tours/',views.TourView.as_view(),name='tours'),
    path('shop/',views.ShopView.as_view(),name='shop'),
    path('uploadtrack/',views.add_track,name='upload'),
    path('addtour/',views.add_tour,name='newtour'),
]