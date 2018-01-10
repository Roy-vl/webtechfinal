from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Meme(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to = 'memes')
    categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta: 
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Category(models.model):
    CATEGORIES = [
        ('CU', 'Cute'),
        ('FU', 'Funny'),
        ('DA', 'Dank'),
        ('OS', 'Only Smart People Will Understand'),
    ]
    title = models.CharField( default = 'DA', max_length = 50, choices = CATEGORIES)
    
    	
class Profile(models.Model):
    CATEGORIES = [
        ('CU', 'Cute'),
        ('FU', 'Funny'),
        ('DA', 'Dank'),
        ('OS', 'Only Smart People Will Understand'),
    ]
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    avater = models.ImageField()
    fb_link = models.URLField()
    seenMemes = models.ManyToManyField('Meme')
    likes = models.ManyToManyField('Category', through='Like')
	top_3_cat = models.CharField(
	    max_length = 50,
	    choices = CATEGORIES,
	    default = 'DA',
    )
	
    def __str__(self):
        return self.user.username
		
class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    meme = models.ForeignKey(Meme, on_delete=models.DO_NOTHING)