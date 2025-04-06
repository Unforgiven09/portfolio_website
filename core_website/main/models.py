from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField (blank=True, verbose_name='Описание')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

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
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    manufacturer = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(null=False, verbose_name='Цена')
    size = models.CharField(max_length=20, blank=True, verbose_name='Габариты')
    weight = models.IntegerField(null=True, verbose_name='Вес')
    extra = models.TextField(blank=True, verbose_name='Дополнительная информация')
    display_diagonal = models.IntegerField(null=True, verbose_name='Диагональ дисплея') # для мониторов и ноутбуков
    brief_technical_specifications = models.TextField(blank=True, verbose_name='Короткие технические характеристики') # для компов и ноутбуков
    buttons = models.IntegerField(null=True, verbose_name='Количество кнопок') # для клавиатур и мышек
    guarantee = models.IntegerField(null=True, verbose_name='Гарантия')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', default=1)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return f'Комментарий к посту "{self.post}" от пользователя "{self.user}"'

    class Meta:
        verbose_name = 'Комментарий к товару'
        verbose_name_plural = 'Комментарии к товару'
        ordering = ['-published_date']


class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=100, blank=True)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info', verbose_name='Информация о пользователе')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    tel = models.CharField(max_length=10, blank=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Почта')