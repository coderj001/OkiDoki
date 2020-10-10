from django.urls import path
from feed.views import feed
from feed.api import api_add_oki


app_name = "feed"

urlpatterns = [
    path('', feed, name="feed"),
    path('api/add_oki/', api_add_oki, name="api_add_oki"),
]
