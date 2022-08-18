from django.urls import path
from musicapp import views


urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('tours/',views.TourView.as_view(),name='tours'),
    path('shop/',views.ShopView.as_view(),name='shop'),
    path('uploadtrack/',views.add_track,name='upload'),
    path('addtour/',views.add_tour,name='newtour'),
    path('administrator/',views.admin,name='admin'),
    path('registration/',views.registration_view,name='registration'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]