from django.conf.urls import url
import feeds

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rss', feeds.LatestSongs()),
]
