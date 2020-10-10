from django.urls import path
from okir_profile.views import okirprofile

app_name = "okirprofile"

urlpatterns = [
    path('<str:username>/', okirprofile, name="okirprofile"),
]
