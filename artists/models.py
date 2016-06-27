from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=64)


class Album(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  image_url = models.CharField(max_length=255)

