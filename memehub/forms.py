from django import forms

from .models import Meme
class PostForm(forms.ModelForm):

    class Meta:
        model = Meme
        fields = ('title', 'image',)
