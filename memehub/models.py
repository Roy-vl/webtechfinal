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
    image = models.ImageField(upload_to = 'memes')
    categories = models.CharField(default = 'DA', max_length = 50, choices = CATEGORIES)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Profile(models.Model):
    CATEGORIES = [
        ('CU', 'Cute'),
        ('FU', 'Funny'),
        ('DA', 'Dank'),
        ('OS', 'Only Smart People Will Understand'),
    ]
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    avater = models.ImageField(upload_to='avatar')
    fb_link = models.URLField()
    seenMemes = models.ManyToManyField('Meme')
    top_3_cat = models.CharField(
	    max_length = 50,
	    choices = CATEGORIES,
	    default = 'DA',
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
