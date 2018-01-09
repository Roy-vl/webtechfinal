from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^meme/new/$', views.new_meme, name='newmeme'),
    url(r'^judge/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
