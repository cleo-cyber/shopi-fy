from unicodedata import name
from django.urls import path
from musicapp import views,accounts,tracks,tour
from shop.views import ShopView


urlpatterns=[
    path('',tracks.IndexView.as_view(),name='index'),
    path('tours/',tour.TourView.as_view(),name='tours'),
    path('shop/',ShopView.as_view(),name='shop'),
    path('uploadtrack/',tracks.add_track,name='upload'),
    path('addtour/',tour.add_tour,name='newtour'),
    path('administrator/',views.admin,name='admin'),
    path('registration/',accounts.registration_view,name='registration'),
    path('login/',accounts.login_view,name='login'),
    path('logout/',accounts.logout_view,name='logout'),
    path('updatetrack/<int:pk>/',tracks.edit_track,name='updatetrack'),
    path('deletetrack/<int:pk>/',tracks.remove_track,name='deletetrack'),
    path('trackadmin/',tracks.AdminViewTracks.as_view(),name='admintracks')
]