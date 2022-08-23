from dataclasses import field, fields
from pyexpat import model
from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from musicapp.models import Account
from django.contrib.auth import authenticate
from shop.models import Product
from .models import Tour, Tracks


class ImageForm(forms.ModelForm):
    track_banner = forms.ImageField()
    title = forms.CharField()

    class Meta:
        model = Tracks
        fields = ['track_banner', 'title']


class TourForm(forms.ModelForm):
    event_description = forms.Textarea()
    venue = forms.CharField()
    price = forms.DecimalField(max_digits=50)
    event_type = forms.CharField(max_length=200)

    class Meta:
        model = Tour
        fields = ['event_description', 'venue', 'price', 'event_type']

class ProductForm(forms.ModelForm):
    product_image=forms.ImageField()
    product_name=forms.CharField(max_length=200)
    price=forms.DecimalField(max_digits=50)

    class Meta:
        model=Product
        fields=['product_image','product_name','price']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Credentials')
