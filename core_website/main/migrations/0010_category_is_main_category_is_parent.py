# Generated by Django 5.1.7 on 2025-04-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_banner_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
    ]
