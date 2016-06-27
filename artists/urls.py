from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^add/$', views.add_artist, name='add_artist'),
  url(r'^process_add_artist/$', views.process_add_artist, name='process_add_artist'),
]
