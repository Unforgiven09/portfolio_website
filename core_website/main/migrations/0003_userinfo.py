# Generated by Django 5.1.7 on 2025-04-05 15:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_description_category_parent_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=10, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL, verbose_name='Информация о пользователе')),
            ],
        ),
    ]
