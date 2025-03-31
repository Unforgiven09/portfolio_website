from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(null=False, verbose_name='Цена')
    size = models.CharField(max_length=20, blank=True, verbose_name='Габариты')
    weight = models.IntegerField(null=False, blank=True, verbose_name='Вес')
    extra = models.TextField(blank=True, verbose_name='Дополнительная информация')
    display_diagonal = models.IntegerField(null=False, blank=True, verbose_name='Диагональ дисплея') # для мониторов и ноутбуков
    brief_technical_specifications = models.TextField(blank=True, verbose_name='Короткие технические характеристики') # для компов и ноутбуков
    buttons = models.IntegerField(null=False, blank=True, verbose_name='Количество кнопок') # для клавиатур и мышек
    guarantee = models.IntegerField(null=False, blank=True, verbose_name='Гарантия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
