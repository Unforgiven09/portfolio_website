from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Posts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(verbose_name='Текст поста')
    published_date = models.DateTimeField(auto_created=True, verbose_name='Дата публикации')
    image = models.URLField(unique=True, default=None, blank=True, verbose_name='Изображение')
    tag = models.ManyToManyField(Tags, related_name='Post', verbose_name='Тег')
    product = models.ManyToManyField('main.Products', related_name='post_product', verbose_name='Товар')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
