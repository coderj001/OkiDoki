from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField

# TODO: Add ckeditor later


class Oki(models.Model):
    body = models.CharField(max_length=255, blank=False)
    # body = RichTextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name="okir", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        if len(self.body) < 25:
            return self.body
        else:
            return f"{self.body[:22]}..."

    # def get_absolute_url(self):
    #     return reverse("",kwargs={'id': self.id})
