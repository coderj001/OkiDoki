from django.contrib.auth.models import User
from django.db import models


class OkirProfile(models.Model):
    okir = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return f"{self.okir}'s profile"


User.okirprofile = property(
    lambda u: OkirProfile.objects.get_or_create(okir=u)[0])
