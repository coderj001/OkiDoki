from django.urls import path, include
from core.views import frontpage

app_name = "core"

urlpatterns = [
    path('', frontpage, name="frontpage"),
]
