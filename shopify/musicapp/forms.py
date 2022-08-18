from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from musicapp.models import Account
from django.contrib.auth import authenticate


class ImageForm(forms.Form):
    track_banner = forms.ImageField()
    title = forms.CharField()


class TourForm(forms.Form):
    event_description = forms.CharField(max_length=200)
    venue = forms.CharField()
    price = forms.DecimalField(max_digits=50)
    event_type = forms.CharField(max_length=200)


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
