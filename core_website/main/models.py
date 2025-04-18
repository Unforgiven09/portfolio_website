import os
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField (blank=True, verbose_name='Описание')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_parent = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    manufacturer = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(null=False, verbose_name='Цена')
    size = models.CharField(max_length=20, blank=True, null=True, verbose_name='Габариты')
    weight = models.IntegerField(null=True, blank=True, verbose_name='Вес')
    extra = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация')
    display_diagonal = models.IntegerField(null=True, blank=True, verbose_name='Диагональ дисплея') # для мониторов и ноутбуков
    brief_technical_specifications = models.TextField(null=True, blank=True, verbose_name='Короткие технические характеристики') # для компов и ноутбуков
    buttons = models.IntegerField(null=True, blank=True, verbose_name='Количество кнопок') # для клавиатур и мышек
    guarantee = models.IntegerField(null=True, blank=True, verbose_name='Гарантия')
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']


class CommentToProduct(models.Model):
    content = models.TextField(verbose_name='Текст комментария')
    post = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return f'Комментарий к посту "{self.post}" от пользователя "{self.user}"'

    class Meta:
        verbose_name = 'Комментарий к товару'
        verbose_name_plural = 'Комментарии к товару'
        ordering = ['-published_date']


class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/', blank=True)
    alt_text = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='products/thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.create_thumbnail()

    def create_thumbnail(self):
        img_path = self.image.path
        thumb_path = os.path.join(os.path.dirname(img_path), 'thumbnails', os.path.basename(img_path))
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
        img.save(thumb_path)
        self.thumbnail = f"products/thumbnails/{os.path.basename(img_path)}"
        super().save(update_fields={'thumbnail'})

    def __str__(self):
        return self.product


class Banner(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='main/banners/', unique=False, null=True, blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор баннера')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name