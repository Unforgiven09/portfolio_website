# Generated by Django 5.1.7 on 2025-04-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_posts_thumbnail_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/', verbose_name='Изображение'),
        ),
    ]
