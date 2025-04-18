import os
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Tags(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']


class Posts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(verbose_name='Текст поста')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста', default=1)
    image = models.ImageField(upload_to='news/', unique=False, null=True, blank=True, verbose_name='Изображение')
    tag = models.ManyToManyField(Tags, related_name='posts', verbose_name='Тег')
    product = models.ManyToManyField('main.Products', related_name='post_products', verbose_name='Товар', blank=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    thumbnail = models.ImageField(upload_to='news/thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        is_new = not self.pk
        super().save(*args, **kwargs)

        if self.image and is_new:
            thumb_path = self.create_thumbnail()
            self.thumbnail = thumb_path
            super().save(update_fields=['thumbnail'])

    def create_thumbnail(self):
        img_path = self.image.path
        thumb_dir = os.path.join(os.path.dirname(img_path), 'thumbnails')
        os.makedirs(thumb_dir, exist_ok=True)
        thumb_path = os.path.join(thumb_dir, os.path.basename(img_path))

        img = Image.open(img_path)
        img.thumbnail((200, 200))
        img.save(thumb_path)

        return f"news/thumbnails/{os.path.basename(img_path)}"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published_date']


class CommentToPost(models.Model):
    content = models.TextField(verbose_name='Текст комментария')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Пост')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return f'Комментарий к посту "{self.post}" от пользователя "{self.user}"'

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Комментарии к посту'
        ordering = ['-published_date']


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Пост', related_name='likes')
    liked_at = models.DateTimeField(auto_now_add=True, verbose_name='Время лайка')

    class Meta:
        unique_together = ('user', 'post')
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f"{self.user.username} лайкнул {self.post.title}"