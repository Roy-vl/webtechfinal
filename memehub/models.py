from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Meme(models.Model):
    CUTE = 'CU',
    FUNNY = 'FU',
    DANK = 'DA',
    ONLYSMARTPPL = 'OS',
    CATEGORIES = [
        (CUTE, 'Cute'),
        (FUNNY, 'Funny'),
        (DANK, 'Dank'),
        (ONLYSMARTPPL, 'Only Smart People Will Understand'),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = './memes')
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.CharField( default = 'DA', max_length = 50, choices = CATEGORIES)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    CUTE = 'CU',
    FUNNY = 'FU',
    DANK = 'DA',
    ONLYSMARTPPL = 'OS',
    CATEGORIES = [
        (CUTE, 'Cute'),
        (FUNNY, 'Funny'),
        (DANK, 'Dank'),
        (ONLYSMARTPPL, 'Only Smart People Will Understand'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avater = models.ImageField()
    fb_link = models.URLField()
    top_3_cat = models.CharField(
	    max_length = 50,
	    choices = CATEGORIES,
	    default = 'DA',
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
