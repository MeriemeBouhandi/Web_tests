from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.portraits_list, name='portraits_list'),
    url(r'^portraits/(?P<pk>[0-9]+)/$', views.portraits_detail, name='portraits_detail'),
    url(r'^portraits/new/$', views.portraits_new, name='portraits_new'),
    url(r'^portraits/(?P<pk>[0-9]+)/commentaire/$', views.add_commentaire_to_portraits, name='add_commentaire_to_portraits'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)