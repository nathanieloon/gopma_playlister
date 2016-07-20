from django.contrib.syndication.views import Feed
from .models import Song

class LatestSongs(Feed):
    title = "GOPMA Songs"
    link = "/"

    def items(self):
        return Song.objects.order_by('-date_added')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return "test description"

    def item_link(self, item):
        return "https://play.google.com/music/m/" + item.tid