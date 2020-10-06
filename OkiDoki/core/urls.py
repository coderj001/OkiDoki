from django.urls import path, include
from core.views import demo

app_name = "core"

urlpatterns = [
    path('demo/', demo, name="demo"),
]
