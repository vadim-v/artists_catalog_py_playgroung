from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^add/$', views.add_artist, name='add_artist'),
  url(r'^browse/$', views.browse_artist, name='browse_artist'),
  url(r'^fetch_albums/(?P<artist_id>[0-9]+)/$', views.fetch_albums, name='fetch_albums'),
  url(r'^search_albums/$', views.search_albums, name='search_albums'),
  url(r'^process_add_artist/$', views.process_add_artist, name='process_add_artist'),
]
