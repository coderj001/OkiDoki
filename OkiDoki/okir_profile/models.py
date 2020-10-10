from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class OkirProfile(models.Model):
    okir = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return f"{self.okir}'s profile"

    def __unicode__(self):
        return f"{self.id}"

    def get_profile_url(self):
        return reverse("okirprofile:okirprofile", kwargs={'username': self.okir.username})

    # TODO: Try creating abs url for follow and unfollow
    # def get_follow_url(self):
    #     return reverse("okirprofile:follow", kwargs={'username': self.okir.username})


User.okirprofile = property(
    lambda u: OkirProfile.objects.get_or_create(okir=u)[0])
