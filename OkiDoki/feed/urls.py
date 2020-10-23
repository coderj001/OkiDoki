from django.urls import path
from feed.views import feed, search
from feed.api import api_add_oki, api_add_doki


app_name = "feed"

urlpatterns = [
    path('', feed, name="feed"),
    path('search/', search, name="search"),

    # API

    path('api/add_oki/', api_add_oki, name="api_add_oki"),
    path('api/add_doki_to_oki/', api_add_doki, name="api_add_doki"),
]
