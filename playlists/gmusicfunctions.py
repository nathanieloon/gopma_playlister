# Gmusic functions
from gmusicapi import Mobileclient
import sys, ConfigParser, pytz
from .models import Playlist
from datetime import datetime, timedelta
from django.utils import timezone

PLAYLIST_PREFIX = '[GOPMA] '

def login():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')

    email = config.get('login', 'email')
    password = config.get('login', 'password')

    print "Logging into Google Play Music as", email
    api = Mobileclient()
    login = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)

    if not login:
        print "<< Couldn't login. >>"
        sys.exit()
    
    return api

def update():
    api = login()
    
    playlists = api.get_all_playlists()
    for pl in playlists:
        if PLAYLIST_PREFIX in pl['name'] and pl['type'] == 'USER_GENERATED':
            time = timezone.make_aware(datetime.fromtimestamp(int(pl['lastModifiedTimestamp'])/1000000))
            p = Playlist(gid = pl['id'], name=pl['name'], share_token=pl['shareToken'], owner=pl['ownerName'], last_updated=time)
            p.save()
            
