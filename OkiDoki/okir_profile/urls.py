from django.urls import path
from okir_profile.views import okirprofile, follow_okir, unfollow_okir

app_name = "okirprofile"

urlpatterns = [
    path('<str:username>/', okirprofile, name="okirprofile"),
    path('<str:username>/follow/', follow_okir, name="follow"),
    path('<str:username>/unfollow/', unfollow_okir, name="unfollow"),
]
