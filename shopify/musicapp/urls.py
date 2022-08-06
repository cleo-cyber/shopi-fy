from django.urls import path
from musicapp import views

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('tours/',views.TourView.as_view(),name='tours')
]