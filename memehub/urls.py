from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^judge/$', views.judge, name='judge'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^register/$', views.register, name='register'),
    url(r'^judge/like/(?P<pk>\d+)/$', views.like, name='like'),
    url(r'^dislike/(?P<pk>\d+)/$', views.dislike, name='dislike'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', views.update_profile, name='profile'),
]
