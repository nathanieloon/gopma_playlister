from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Playlist(models.Model):
    gid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField()
    owner = models.CharField(max_length=100)
    share_token = models.CharField(max_length=100)
