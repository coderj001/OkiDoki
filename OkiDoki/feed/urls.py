from django.urls import path
from feed.views import feed


app_name = "feed"

urlpatterns = [
    path('', feed, name="feed"),
]
