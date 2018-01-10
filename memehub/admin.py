from django.contrib import admin
from memehub import models
 
admin.site.register(models.Meme) #Register the model with the admin
admin.site.register(models.Profile) #Register the model with the admin
admin.site.register(models.Like) #Register the model with the admin
admin.site.register(models.Category) #Register the model with the admin
