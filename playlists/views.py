from django.shortcuts import render
from gmusicapi import Mobileclient

from .models import Playlist
from gmusicfunctions import update
from datetime import timedelta
from django.utils import timezone

last_update = timezone.now() - timedelta(minutes=15)

# Create your views here.
def index(request):
    global last_update
    time_diff = timezone.now() - last_update
    if (time_diff.seconds//60)%60 >= 2:
        update()
        last_update = timezone.now()
    playlists = Playlist.objects.order_by('name')
    context = {
        'playlists': playlists,
    }
    return render(request, 'playlists/index.html', context)
