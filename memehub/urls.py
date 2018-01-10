from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
	path('accounts/', include('django.contrib.auth.urls')),
    url(r'^judge/$', views.judge, name='judge'),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/profile$', views.update_profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
