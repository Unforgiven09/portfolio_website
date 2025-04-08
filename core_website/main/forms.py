from django import forms
from .models import Category


class CatsForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug',)