from django import forms
from .models import Posts, Tags, CommentToPost


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('published_date', 'slug', 'user', 'likes', 'thumbnail')


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        exclude = ('slug',)


class CommentToPostForm(forms.ModelForm):
    class Meta:
        model = CommentToPost
        exclude = ('published_date', 'user', 'post', )
