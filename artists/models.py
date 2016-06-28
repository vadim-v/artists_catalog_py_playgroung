from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=64)

  def __str__(self):
  	return self.name


class Album(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  image_url = models.CharField(max_length=255)
  release_date = models.DateTimeField('date released')

  def __str__(self):
  	return self.name

