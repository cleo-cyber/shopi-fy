from django.urls import path
from musicapp import views

urlpatterns=[
    path('',views.hello,name='hello')
]