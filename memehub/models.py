from django.db import models
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Meme(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.CharField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avater = models.ImageField()
    fb_link = models.URLField()
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    top_3_cat = models_Charfield(
    choiches = TEST
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


