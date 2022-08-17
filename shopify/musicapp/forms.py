from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from musicapp.models import Account
class ImageForm(forms.Form):
    track_banner=forms.ImageField()
    title=forms.CharField()

class TourForm(forms.Form):
    event_description=forms.CharField(max_length=200)
    venue=forms.CharField()
    price=forms.DecimalField(max_digits=50)
    event_type=forms.CharField(max_length=200)

class RegistrationForm(UserCreationForm):
    class Meta:
        model=Account
        fields=('email','username','password1','password2')
