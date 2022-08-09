from django import forms

class ImageForm(forms.Form):
    track_banner=forms.ImageField()
    title=forms.CharField()