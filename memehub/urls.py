from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	path('accounts/', include('django.contrib.auth.urls')),
    url(r'^judge/$', views.judge, name='judge'),
]
