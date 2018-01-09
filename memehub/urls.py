from django.conf.urls import url
from . import views
from . import views as core_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', core_views.register, name='register'),
]
