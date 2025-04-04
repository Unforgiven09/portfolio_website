# Generated by Django 5.1.7 on 2025-04-01 08:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Текст поста')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('image', models.URLField(blank=True, null=True, unique=True, verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True)),
                ('product', models.ManyToManyField(blank=True, related_name='post_products', to='main.products', verbose_name='Товар')),
                ('tag', models.ManyToManyField(related_name='posts', to='news.tags', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='CommentToPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Текст комментария')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.posts', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарий к посту',
                'verbose_name_plural': 'Комментарии к посту',
                'ordering': ['-published_date'],
            },
        ),
    ]
