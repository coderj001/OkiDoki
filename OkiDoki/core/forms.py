from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password incorrect.')
            if not user.check_password(password):
                raise forms.ValidationError('Not password incorrect')
            if not user.is_active:
                raise forms.ValidationError('plus valide')
        return super().clean(*args, **kwargs)
