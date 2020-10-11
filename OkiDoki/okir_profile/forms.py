from django import forms

from okir_profile.models import OkirProfile


class OkirProfileForm(forms.ModelForm):
    class Meta:
        model = OkirProfile
        fields = ('avatar',)
