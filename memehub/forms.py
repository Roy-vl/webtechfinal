from django import forms

from .models import Meme, Profile
class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ('title', 'image', 'categories')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fb_link', 'avater')
