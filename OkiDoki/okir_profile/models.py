from django.db import models
from django.contrib.auth.models import User


class OkirProfile(models.Model):
    okir = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False)


User.okirprofile = property(
    lambda u: OkirProfile.objects.get_or_create(user=u)[0])
