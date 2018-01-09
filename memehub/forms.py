from django import forms

from .models import Post
from .models import Todo
class PostForm(forms.ModelForm):

    class Meta:
        model = Meme
        fields = ('title', 'image',)
