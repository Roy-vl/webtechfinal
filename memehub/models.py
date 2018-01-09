from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Meme(models.Model):
    CATEGORIES = [
        ('CU', 'Cute'),
        ('FU', 'Funny'),
        ('DA', 'Dank'),
        ('OS', 'Only Smart People Will Understand'),
    ]
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to = './memes')
    categories = models.CharField( default = 'DA', max_length = 50, choices = CATEGORIES)

    def __str__(self):
        return self.title

class Profile(models.Model):
    CATEGORIES = [
        ('CU', 'Cute'),
        ('FU', 'Funny'),
        ('DA', 'Dank'),
        ('OS', 'Only Smart People Will Understand'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avater = models.ImageField()
    fb_link = models.URLField()
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(max_length = 2, null=True, blank=True)
    top_3_cat = models.CharField(
	    max_length = 50,
	    choices = CATEGORIES,
	    default = 'DA',
    )
	
    def __str__(self):
        return self.title 

