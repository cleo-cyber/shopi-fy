from django import forms

class ImageForm(forms.Form):
    track_banner=forms.ImageField()
    title=forms.CharField()

class TourForm(forms.Form):
    event_description=forms.CharField(max_length=200)
    venue=forms.CharField()
    price=forms.DecimalField(max_digits=50)
    event_type=forms.CharField(max_length=200)

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()