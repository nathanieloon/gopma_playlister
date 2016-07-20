from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Playlist(models.Model):
    gid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    share_token = models.CharField(max_length=100)
    last_updated = models.DateTimeField()

class Song(models.Model):
    tid = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    date_added = models.DateTimeField()