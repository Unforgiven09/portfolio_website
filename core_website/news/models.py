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
    image = models.URLField(unique=True, null=True, blank=True, verbose_name='Изображение')
    tag = models.ManyToManyField(Tags, related_name='posts', verbose_name='Тег')
    product = models.ManyToManyField('main.Products', related_name='post_products', verbose_name='Товар', blank=True)
    likes = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published_date']


class CommentToPost(models.Model):
    content = models.TextField(verbose_name='Текст комментария')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Пост')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', default=1)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return f'Комментарий к посту "{self.post}" от пользователя "{self.user}"'

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Комментарии к посту'
        ordering = ['-published_date']
