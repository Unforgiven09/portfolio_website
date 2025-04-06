from django import forms
from .models import UserInfo


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('user',)