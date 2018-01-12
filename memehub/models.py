from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    CATEGORIES = [
        ('CU', 'Cute'),
        ('FU', 'Funny'),
        ('DA', 'Dank'),
        ('OS', 'Only Smart People Will Understand'),
    ]
    title = models.CharField( default = 'DA', max_length = 50, choices = CATEGORIES)
	
    def __str__(self):
        return self.title


class Meme(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to = 'memes')
    categories = models.ForeignKey(Category, related_name="cat_of_meme" ,on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    avater = models.ImageField(upload_to='avatar', default='/avatar/default.jpg')
    fb_link = models.URLField(default = 'Https://facebook.com')
    seenMemes = models.ManyToManyField('Meme')
    likes = models.ManyToManyField('Category', through='Like')
    top_cat = models.ForeignKey(Category, related_name="user_most_liked", default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    class Meta: 
        ordering = ['amount']
    def __str__(self):
        return self.profile.user.username+self.category.title
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

