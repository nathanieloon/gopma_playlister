from django.contrib.syndication.views import Feed
from .models import Song
from gmusicfunctions import PLAYLIST_PREFIX

class LatestSongs(Feed):
    title = PLAYLIST_PREFIX + "Feed"
    link = "/"

    def items(self):
        return Song.objects.order_by('-date_added')

    def item_title(self, item):
        return item.title + " by " + item.artist

    def item_description(self, item):
        return "The genre of this song is " + item.genre + "."

    def item_link(self, item):
        return "https://play.google.com/music/m/" + item.tid